import typer

from powerbi_cli.dataset import refresh
from powerbi_cli.dataset.get import get
from powerbi_cli.dataset.list import list

# from .list import command as list_command

app = typer.Typer()

app.add_typer(refresh.app, name="refresh")

app.command(name="list")(list)
app.command(name="get")(get)
