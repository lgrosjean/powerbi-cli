import click

from powerbi_cli.client import get_client


@click.command()
@click.option("-w", "--workspace", default=None)
@click.option(
    "--notify",
    type=click.Choice(["MailOnCompletion", "MailOnFailure", "NoNotification"]),
    default="NoNotification",
    show_default=True,
)
@click.option(
    "--type",
    "type_",
    type=click.Choice(
        ["Automatic", "Calculate", "ClearValues", "DataOnly", "Defragment", "Full"]
    ),
    default=None,
    show_default=True,
)
@click.argument("dataset")
def start(
    dataset,
    workspace,
    type_,
    notify,
):
    """Triggers a refresh for the specified dataset from the specified workspace."""
    pbi = get_client()

    click.echo(f"{type_}, {notify}")

    endpoint = f"/datasets/{dataset}/refreshes"
    if workspace:
        endpoint = f"groups/{workspace}/" + endpoint

    dataset_ = pbi.dataset(dataset=dataset, group=workspace)
    dataset_.refresh(notify_option=notify, type=type_)
