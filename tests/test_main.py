from click.testing import CliRunner

from powerbi_cli.main import pbi


def test_pbi():
    runner = CliRunner()
    result = runner.invoke(pbi)
    assert result.exit_code == 0
    assert "Usage: pbi [OPTIONS] COMMAND [ARGS]..." in result.output
    assert "admin" in result.output
    assert "auth" in result.output
    assert "dataset" in result.output
    assert "report" in result.output
    assert "workspace" in result.output


def test_pbi_admin():
    runner = CliRunner()
    result = runner.invoke(pbi, "admin")
    assert result.exit_code == 0


def test_pbi_auth():
    runner = CliRunner()
    result = runner.invoke(pbi, "auth")
    assert result.exit_code == 0
