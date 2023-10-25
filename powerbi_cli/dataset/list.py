import click
from tabulate import tabulate

from powerbi_cli.client import get_client


@click.command(name="list")
@click.option("-w", "--workspace", type=str, default=None, show_default=True)
def list_(workspace: str):
    """List Dataset in given workspace"""
    pbi = get_client()
    datasets = pbi.datasets(group=workspace)
    table = [
        [dataset.id, dataset.name, dataset.configured_by, dataset.created_date]  # type: ignore
        for dataset in datasets
    ]
    headers = ["DATASET ID", "NAME", "CONFIGURED BY", "CREATED DATE"]
    click.echo(tabulate(table, headers, tablefmt="simple"))
