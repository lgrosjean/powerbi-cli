from click.testing import CliRunner

from powerbi_cli.main import powerbi


def test_pbi():
    runner = CliRunner()
    result = runner.invoke(powerbi)
    assert result.exit_code == 0
    assert "Usage: powerbi [OPTIONS] COMMAND [ARGS]..." in result.output
    assert "admin" in result.output
    assert "auth" in result.output
    assert "dataset" in result.output
    assert "report" in result.output
    assert "workspace" in result.output


def test_pbi_admin():
    runner = CliRunner()
    result = runner.invoke(powerbi, "admin")
    assert result.exit_code == 0


def test_pbi_auth():
    runner = CliRunner()
    result = runner.invoke(powerbi, "auth")
    assert result.exit_code == 0
