import click

from powerbi_cli.auth.token import token


@click.group()
def auth():
    """Interact with PowerBI Auth"""


auth.add_command(token)
