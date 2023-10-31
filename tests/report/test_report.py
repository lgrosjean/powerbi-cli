from click.testing import CliRunner

from powerbi_cli.report.main import report


def test_report():
    runner = CliRunner()
    result = runner.invoke(report)
    assert result.exit_code == 0
    assert "export" in result.output
    assert "get" in result.output
    assert "list" in result.output
    assert "open" in result.output
