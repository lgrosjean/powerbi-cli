import click

from .admin import admin
from .auth import auth
from .dataset import dataset
from .report import report
from .workspace import workspace


@click.group()
def pbi():
    """Base PowerBI CLi entrypoint"""


pbi.add_command(dataset)
pbi.add_command(workspace)
pbi.add_command(auth)
pbi.add_command(report)
pbi.add_command(admin)
