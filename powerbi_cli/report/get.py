import click
from tabulate import tabulate

from powerbi_cli.client import pbi


@click.command()
@click.option("-w", "--workspace", default=None)
@click.argument("report")
def get(report: str, workspace: str):
    """Get details about one Dataset in a given workspace"""
    report_ = pbi.report(report=report, group=workspace)

    table = [[k, v] for k, v in report_.raw.items()]  # type: ignore
    click.echo(tabulate(table, tablefmt="plain"))
