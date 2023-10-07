import click
from tabulate import tabulate

from powerbi_cli.client import get_client


@click.command(name="list")
@click.argument("workspace", type=str, default=None)
def list_(workspace: str):
    """List Reports in given workspace"""
    pbi = get_client()
    reports = pbi.reports(group=workspace)
    click.echo(reports)
    table = [
        [report.id, report.name, report.group_id, report.dataset_id]  # type: ignore
        for report in reports
    ]
    headers = ["REPORT ID", "NAME", "WORKSPACE ID", "DATASET ID"]
    click.echo(tabulate(table, headers, tablefmt="simple"))
