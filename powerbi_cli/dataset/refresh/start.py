import click


@click.command()
def start(
    dataset,
    workspace,
    type,
    notify,
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
    # typer.echo(body)
    # typer.echo(res.json())
