import click

from .admin import admin
from .auth import auth
from .dataset import dataset
from .report import report
from .workspace import workspace


@click.group()
def powerbi():
    """Base PowerBI CLI entrypoint"""


powerbi.add_command(dataset)
powerbi.add_command(workspace)
powerbi.add_command(auth)
powerbi.add_command(report)
powerbi.add_command(admin)


if __name__ == "__main__":
    powerbi()
