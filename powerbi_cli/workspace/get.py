import json

import click

from powerbi_cli.client import pbi


@click.command()
@click.argument("workspace")
def get(workspace: str):
    """Get details about one Dataset in a given workspace"""
    group = pbi.group(group_id=workspace)
    click.echo(json.dumps(group.raw, indent=2))
