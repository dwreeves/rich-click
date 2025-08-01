import sys
from gettext import gettext
from typing import TYPE_CHECKING, Any, Callable, Dict, Mapping, Optional, Type, TypeVar, Union, cast, overload

from click import Command, Context, Group, Parameter
from click import command as click_command
from click import option as click_option
from click import pass_context as click_pass_context

from rich_click.rich_command import RichCommand, RichGroup
from rich_click.rich_context import RichContext
from rich_click.rich_help_configuration import RichHelpConfiguration

from . import rich_click  # noqa: F401


if sys.version_info < (3, 10):
    from typing_extensions import Concatenate, ParamSpec
else:
    from typing import Concatenate, ParamSpec


if TYPE_CHECKING:  # pragma: no cover
    from rich.console import Console


_AnyCallable = Callable[..., Any]
F = TypeVar("F", bound=Callable[..., Any])
FC = TypeVar("FC", bound=Union[Command, _AnyCallable])


GrpType = TypeVar("GrpType", bound=Group)


# variant: no call, directly as decorator for a function.
@overload
def group(name: _AnyCallable) -> RichGroup: ...


# variant: with positional name and with positional or keyword cls argument:
# @group(namearg, GroupCls, ...) or @group(namearg, cls=GroupCls, ...)
@overload
def group(
    name: Optional[str],
    cls: Type[GrpType],
    **attrs: Any,
) -> Callable[[_AnyCallable], GrpType]: ...


# variant: name omitted, cls _must_ be a keyword argument, @group(cmd=GroupCls, ...)
@overload
def group(
    name: None = None,
    *,
    cls: Type[GrpType],
    **attrs: Any,
) -> Callable[[_AnyCallable], GrpType]: ...


# variant: with optional string name, no cls argument provided.
@overload
def group(name: Optional[str] = ..., cls: None = None, **attrs: Any) -> Callable[[_AnyCallable], RichGroup]: ...


def group(
    name: Union[str, _AnyCallable, None] = None,
    cls: Optional[Type[GrpType]] = None,
    **attrs: Any,
) -> Union[Group, Callable[[_AnyCallable], Union[RichGroup, GrpType]]]:
    """
    Group decorator function.

    Defines the group() function so that it uses the RichGroup class by default.
    """
    if cls is None:
        cls = cast(Type[GrpType], RichGroup)

    if callable(name):
        return command(cls=cls, **attrs)(name)

    return command(name, cls, **attrs)


CmdType = TypeVar("CmdType", bound=Command)


# variant: no call, directly as decorator for a function.
@overload
def command(name: _AnyCallable) -> RichCommand: ...


# variant: with positional name and with positional or keyword cls argument:
# @command(namearg, CommandCls, ...) or @command(namearg, cls=CommandCls, ...)
@overload
def command(
    name: Optional[str],
    cls: Type[CmdType],
    **attrs: Any,
) -> Callable[[_AnyCallable], CmdType]: ...


# variant: name omitted, cls _must_ be a keyword argument, @command(cls=CommandCls, ...)
@overload
def command(
    name: None = None,
    *,
    cls: Type[CmdType],
    **attrs: Any,
) -> Callable[[_AnyCallable], CmdType]: ...


# variant: with optional string name, no cls argument provided.
@overload
def command(name: Optional[str] = ..., cls: None = None, **attrs: Any) -> Callable[[_AnyCallable], RichCommand]: ...


def command(
    name: Union[Optional[str], _AnyCallable] = None,
    cls: Optional[Type[CmdType]] = None,
    **attrs: Any,
) -> Union[Command, Callable[[_AnyCallable], Union[RichCommand, CmdType]]]:
    """
    Command decorator function.

    Defines the command() function so that it uses the RichCommand class by default.
    """
    if cls is None:
        cls = cast(Type[CmdType], RichCommand)

    if callable(name):
        return click_command(cls=cls, **attrs)(name)

    return click_command(name, cls=cls, **attrs)


class NotSupportedError(Exception):
    """Not Supported Error."""

    pass


def rich_config(
    help_config: Optional[Union[Mapping[str, Any], RichHelpConfiguration]] = None,
    *,
    console: Optional["Console"] = None,
) -> Callable[[FC], FC]:
    """
    Use decorator to configure Rich Click settings.

    Args:
    ----
        help_config: Rich help configuration that is used internally to format help messages and exceptions
            Defaults to None.
        console: A Rich Console that will be accessible from the `RichContext`, `RichCommand`, and `RichGroup` instances
            Defaults to None.

    """
    from rich.console import Console

    if isinstance(help_config, Console) and console is None:
        import warnings

        warnings.warn(
            "`rich_config()`'s args have been swapped."
            " Please set the config first, and use a kwarg to set the console.",
            DeprecationWarning,
            stacklevel=2,
        )
        console = help_config

    def decorator(obj: FC) -> FC:
        extra: Dict[str, Any] = {}
        if console is not None:
            extra["rich_console"] = console
        if help_config is not None:
            extra["rich_help_config"] = help_config

        if isinstance(obj, (RichCommand, RichGroup)):
            obj.context_settings.update(extra)
        elif callable(obj) and not isinstance(obj, (Command, Group)):
            if hasattr(obj, "__rich_context_settings__"):
                obj.__rich_context_settings__.update(extra)
            else:
                setattr(obj, "__rich_context_settings__", extra)
        else:
            raise NotSupportedError("`rich_config` requires a `RichCommand` or `RichGroup`. Try using the cls keyword")
        return obj

    return decorator


# Users of rich_click would face issues using mypy with this code,
# if not for wrapping `pass_context` with a new function signature:
#
# @click.command()
# @click.pass_context
# def cli(ctx: click.RichContext) -> None:
#    ...


P = ParamSpec("P")
R = TypeVar("R")


def pass_context(f: Callable[Concatenate[RichContext, P], R]) -> Callable[P, R]:
    # flake8: noqa: D400,D401
    """Marks a callback as wanting to receive the current context object as first argument."""
    return click_pass_context(f)  # type: ignore[arg-type]


def help_option(*param_decls: str, **kwargs: Any) -> Callable[[FC], FC]:
    """
    Pre-configured ``--help`` option which immediately prints the help page
    and exits the program.

    :param param_decls: One or more option names. Defaults to the single
        value ``"--help"``.
    :param kwargs: Extra arguments are passed to :func:`option`.
    """

    def show_help(ctx: Context, param: Parameter, value: bool) -> None:
        """Callback that print the help page on ``<stdout>`` and exits."""
        if value and not ctx.resilient_parsing:
            # Avoid click.echo() because it ignores console settings like force_terminal.
            # Also, do not print() if empty string; assume console was record=False.
            print(ctx.get_help())
            ctx.exit()

    if not param_decls:
        param_decls = ("--help",)

    kwargs.setdefault("is_flag", True)
    kwargs.setdefault("expose_value", False)
    kwargs.setdefault("is_eager", True)
    kwargs.setdefault("help", gettext("Show this message and exit."))
    kwargs.setdefault("callback", show_help)

    return click_option(*param_decls, **kwargs)
