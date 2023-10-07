from pathlib import Path

import click

from powerbi_cli.client import get_client


@click.command()
@click.option("-w", "--workspace", default=None)
@click.option("-o", "--output", type=click.Path(), default=None)
@click.argument("report")
def export(workspace: str, output: Path, report: str):
    """Download the report as `.pbix` or `.rdl` depending on the report"""
    pbi = get_client()
    report_ = pbi.report(report=report, group=workspace)

    save_to, file_name = None, None

    if output:
        save_to = str(output.parent)
        file_name = str(output.name)

        if not file_name.endswith(".pbix"):
            raise AttributeError("Filename must ends with '.pbix'.")

    report_.download(save_to=save_to, file_name=file_name)  # type: ignore

    click.echo("Report exported!")
