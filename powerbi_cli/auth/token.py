import click

from powerbi_cli.client import get_token


@click.command()
def token():
    """Print the auth token"""
    click.echo(get_token())
