import click

from powerbi_cli.dataset.refresh.start import start


@click.group()
def refresh():
    """Interact with PowerBI Dataset Refresh"""


refresh.add_command(start)
