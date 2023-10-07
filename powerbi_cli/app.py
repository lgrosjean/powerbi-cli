import typer

from . import dataset

app = typer.Typer(name="pbi")

app.add_typer(dataset.app, name="dataset", help="hello")
