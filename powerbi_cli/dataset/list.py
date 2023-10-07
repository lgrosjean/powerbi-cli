import typing as t

import typer

from powerbi_cli.client import client


# TODO: use workspace id or workspace name
def list(workspace: t.Annotated[str, typer.Option("-w", "--workspace")]):
    endpoint = "datasets"
    if workspace:
        endpoint = f"groups/{workspace}/datasets"
    res = client.get(endpoint)
    typer.echo(res.json()["value"])
