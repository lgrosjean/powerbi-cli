import click
from tabulate import tabulate

from powerbi_cli.client import get_client


@click.command()
@click.option("-w", "--workspace", default=None)
@click.argument("report")
def get(report: str, workspace: str):
    """Get details about one Dataset in a given workspace"""
    pbi = get_client()
    report_ = pbi.report(report=report, group=workspace)

    table = [[k, v] for k, v in report_.raw.items()]  # type: ignore
    click.echo(tabulate(table, tablefmt="plain"))
