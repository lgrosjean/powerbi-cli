import typing as t
from enum import Enum

import typer

from powerbi_cli.client import client


class DatasetRefreshType(str, Enum):
    Automatic = "Automatic"
    Calculate = "Calculate"
    Full = "Full"


class NotifyOption(str, Enum):
    always = "always"
    failure = "failure"
    none = "none"


# TODO: use workspace id or workspace name
def start(
    dataset: t.Annotated[str, typer.Argument()],
    workspace: t.Annotated[t.Optional[str], typer.Option("-w", "--workspace")] = None,
    type: DatasetRefreshType = DatasetRefreshType.Full,
    notify: NotifyOption = NotifyOption.always,
):
    """Triggers a refresh for the specified dataset from the specified workspace."""
    endpoint = f"/datasets/{dataset}/refreshes"
    if workspace:
        endpoint = f"groups/{workspace}/" + endpoint

    notify_option = (
        "MailOnCompletion"
        if notify == "always"
        else "MailOnFailure"
        if notify == "failyre"
        else "NoNotification"
    )

    body = {"notifyOption": notify_option}

    # res = client.post(endpoint)
    typer.echo(body)
    # typer.echo(res.json())
