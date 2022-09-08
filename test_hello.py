from click.testing import CliRunner
from hello import marco


def test_marco():
    runner = CliRunner()
    result = runner.invoke(marco, ["--name", "Marco"])
    assert result.exit_code == 0
    assert "Polo" in result.output