#
# https://click.palletsprojects.com/en/8.0.x/testing/

import sys
from pathlib import Path

from click.testing import CliRunner

from src.main import sum

module_name = None
package_name = None
_private_module = None

ClassName = None
_PrivateClass = None
ExceptionName = None


def method_name(function_parameter):  # functions, methods
    pass


def _private_method(_prviate_method_parameter):
    pass


GLOBAL_CONSTANT_NAME = None
CLASS_CONSTANT_NAME = None
_PRIVATE_GLOBAL_CONSTANT = None

global_var_name = None
instance_var_name = None
local_var_name = None
_private_variable = None

i = 0  # counter
e = False  # try/except statements
f = Path()  # file handle in 'with' statements


def test_sum():
    runner = CliRunner()
    result = runner.invoke(sum, ["2", "3"])
    assert result.exit_code == 0
    assert str(5) in result.output

    result = runner.invoke(sum, ["--", "2", "3", "-1"])
    assert result.exit_code == 0
    assert str(4) in result.output
