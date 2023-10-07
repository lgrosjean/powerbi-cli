import click

from powerbi_cli.client import _TOKEN


@click.command()
def token():
    """Print the auth token"""
    click.echo(_TOKEN)
