import json

import click

from powerbi_cli.client import get_client


@click.command()
@click.argument("workspace")
def get(workspace: str):
    """Get details about one Dataset in a given workspace"""
    pbi = get_client()
    group = pbi.group(group_id=workspace)
    click.echo(json.dumps(group.raw, indent=2))
