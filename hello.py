# hello.py
import os

if os.getenv("USE_RC") == "true":
    import rich_click as click
else:
    import click


@click.group()
def cli():
    """my group"""


@cli.command(deprecated=True)
def subcommand():
    """my command"""


cli()
