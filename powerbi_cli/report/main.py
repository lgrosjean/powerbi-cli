import click

from powerbi_cli.report.export import export
from powerbi_cli.report.get import get
from powerbi_cli.report.list import list_
from powerbi_cli.report.open import open_


@click.group()
def report():
    """Interact with PowerBI Reports"""


report.add_command(list_)
report.add_command(get)
report.add_command(export)
report.add_command(open_)
