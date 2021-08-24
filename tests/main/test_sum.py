# https://click.palletsprojects.com/en/8.0.x/testing/

from click.testing import CliRunner
from src.main import sum


def test_sum():
    runner = CliRunner()
    result = runner.invoke(sum, ['--items', 2, 3])
    assert result.exit_code == 0
    assert str(5) in result.output
