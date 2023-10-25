import click

from powerbi_cli.dataset.get import get
from powerbi_cli.dataset.list import list_
from powerbi_cli.dataset.query import query_
from powerbi_cli.dataset.refresh import refresh


@click.group()
def dataset():
    """Interact with PowerBI Dataset"""


dataset.add_command(get)
dataset.add_command(list_)
dataset.add_command(refresh)
dataset.add_command(query_)
