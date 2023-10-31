import click
from tabulate import tabulate

from powerbi_cli.client import get_client


@click.command(name="list")
@click.option("--top", type=int, default=None, show_default=True)
def list_(top: int):
    """List workspaces available"""
    pbi = get_client()
    groups = pbi.groups(top=top)
    table = [[group.id, group.name] for group in groups]  # type: ignore
    headers = ["WORKSPACE ID", "NAME"]
    click.echo()
    click.echo(tabulate(table, headers, tablefmt="simple"))
