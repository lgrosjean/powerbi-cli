import click
from tabulate import tabulate

from powerbi_cli.client import pbi


@click.command()
@click.option("--top", type=int, default=None, show_default=True)
def list_(top: int):
    """List workspaces available"""
    groups = pbi.groups(top=top)
    table = [[group.id, group.name] for group in groups]  # type: ignore
    headers = ["WORKSPACE ID", "NAME"]
    click.echo()
    click.echo(tabulate(table, headers, tablefmt="simple"))
