import click

from powerbi_cli.workspace.get import get
from powerbi_cli.workspace.list import list_


@click.group()
def workspace():
    """Interact with PowerBI Workspace"""


workspace.add_command(list_, name="list")
workspace.add_command(get)
