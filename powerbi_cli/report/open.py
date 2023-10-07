import webbrowser

import click


@click.command(name="open")
@click.option("-w", "--workspace", default=None)
@click.argument("report")
def open_(report: str, workspace: str):
    """Open a given report in the web browser"""
    if not workspace:
        workspace = "me"
    url = f"https://app.powerbi.com/groups/{workspace}/reports/{report}"

    webbrowser.open(url)
