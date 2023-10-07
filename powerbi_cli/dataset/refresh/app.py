import typer

from powerbi_cli.dataset.refresh.start import start

app = typer.Typer()

app.command(name="start")(start)
