import rich_click as click


@click.group()
@click.option(
    "--debug/--no-debug",
    "-d/-n",
    default=False,
    help="""Enable debug mode.
    Newlines are removed by default.

    Double newlines are preserved.""",
)
def cli(debug: bool) -> None:
    """
    My amazing tool does all the things.

    This is a minimal example based on documentation
    from the 'click' package.

    You can try using --help at the top level and also for
    specific subcommands.

    Here are things you can do:

    - sync files
    - download files
    - print help text!

    ... and more!
    """
    print(f"Debug mode is {'on' if debug else 'off'}")


@cli.command()
@click.option(
    "--type",
    required=True,
    default="files",
    show_default=True,
    help="Type of file to sync",
)
@click.option("--all", is_flag=True)
def sync(type: str, all: bool) -> None:
    """Synchronise all your files between two places.
    Example command that doesn't do much except print to the terminal."""
    print("Syncing")


@cli.command(short_help="Optionally use short-help for the group help text")
@click.option("--all", is_flag=True, help="Get everything")
def download(all: bool) -> None:
    """
    Pretend to download some files from
    somewhere. Multi-line help strings are unwrapped
    until you use a double newline.

    Only the first paragraph is used in group help texts.
    Don't forget you can opt-in to rich and markdown formatting!

    \b
    Click escape markers should still work.
      * So you
      * Can keep
      * Your newlines

    And this is a paragraph
    that will be rewrapped again.

    \f
    Also if you want to write function help text that won't
    be rendered to the terminal.
    """
    print("Downloading")


if __name__ == "__main__":
    cli()
