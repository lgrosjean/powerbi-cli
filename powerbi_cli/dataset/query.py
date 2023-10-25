import time

import click
import structlog

from powerbi_cli.client import get_client


@click.command(name="query")
@click.option(
    "-w",
    "--workspace",
    type=str,
    default=None,
    envvar="WORKSPACE_ID",
    show_default=True,
    show_envvar=True,
)
@click.option(
    "-d",
    "--dataset",
    type=str,
    required=True,
    envvar="DATASET_ID",
    show_default=True,
    show_envvar=True,
)
@click.argument("query")
def query_(workspace: str, dataset: str, query: str):
    """Execute a DAX query against the Power BI XMLA endpoint"""
    pbi = get_client()
    dataset_ = pbi.dataset(
        dataset=dataset,
        group=workspace,
    )
    pbi.logger.info(query, dataset=dataset_)
    start = time.perf_counter()
    dax_result = dataset_.execute_queries(queries=query)
    end = time.perf_counter()
    duration = end - start
    click.echo(f"Duration: {duration}")
    click.echo(dax_result)
