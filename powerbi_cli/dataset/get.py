import typing as t

import typer

from powerbi_cli.client import client


# TODO: use workspace id or workspace name
def get(
    dataset: t.Annotated[str, typer.Argument()],
    workspace: t.Annotated[t.Optional[str], typer.Option("-w", "--workspace")] = None,
):
    endpoint = f"datasets/{dataset}"
    if workspace:
        endpoint = f"groups/{workspace}/" + endpoint
    res = client.get(endpoint)
    typer.echo(res.json())
