"""Integrated tests for the Difference Generator Module (diff_logic.py).

This module validates generate_diff(), which compares two structured
configuration files and reports their differences in a user-selected format.

The integrated tests cover 8 cases, each of which is checked against two
user-selected formats - stylish (default) and plain:
Case 1: Comparing two flat .json files;
Case 2: Comparing two nested .json files;
Case 3: Comparing two flat .yml files;
Case 4: Comparing two nested .yml files;
Case 5: Comparing two flat .yaml files;
Case 6: Comparing two nested .yaml files;
Case 7: Unsupported formatter type;
Case 8: Unsupported file format.

The tests are integrated because generate_diff() is basically a composite
function that wraps around a number of functions, which form a pipeline.
These functions are:
1) read_file() => reads and parses config files of .json and .yml / .yaml types into Python dicts;
2) build_diff() = > reads two Python dicts, compares them and generates a diff tree;
3) format_stylish() => reads a diff tree and outputs a 'stylish' string representation of the differences;
4) format_plain() => reads a diff tree and output a 'plain' string representation of the differences.

NOTE: format_stylish(), format_plain() are selected by the user, with the former being the default option.
"""

import pytest
import re
from gendiff.diff_logic import generate_diff
from pathlib import Path
from .helpers import _get_test_data_path, _read_test_file


# INTEGRATED TESTS
# Formatter type is a parameter passed to each function
parametrize_output_formats = pytest.mark.parametrize("format_name", ["stylish", "plain"])


# Case 1: Comparing two flat .json files
@parametrize_output_formats
def test_generate_diff_flat_json(format_name) -> None:
	# Arrange
	file1 = _get_test_data_path("file1_flat.json")
	file2 = _get_test_data_path("file2_flat.json")

	expected_output = _read_test_file(f"expected_{format_name}_flat.txt")

	# Act
	actual_output = generate_diff(file1, file2, format_name)

	# Assert
	assert actual_output == expected_output


# Case 2: Comparing two nested .json files
@parametrize_output_formats
def test_generate_diff_nest_json(format_name) -> None:
	# Arrange
	file1 = _get_test_data_path("file1_nest.json")
	file2 = _get_test_data_path("file2_nest.json")

	expected_output = _read_test_file(f"expected_{format_name}_nest.txt")

	# Act
	actual_output = generate_diff(file1, file2, format_name)

	# Assert
	assert actual_output == expected_output


# Case 3: Comparing two flat .yml files
@parametrize_output_formats
def test_generate_diff_flat_yml(format_name) -> None:
	# Arrange
	file1 = _get_test_data_path("file1_flat.yml")
	file2 = _get_test_data_path("file2_flat.yml")

	expected_output = _read_test_file(f"expected_{format_name}_flat.txt")

	# Act
	actual_output = generate_diff(file1, file2, format_name)

	# Assert
	assert actual_output == expected_output


# Case 4: Comparing two nested .yml files
@parametrize_output_formats
def test_generate_diff_nest_yml(format_name) -> None:
	# Arrange
	file1 = _get_test_data_path("file1_nest.yml")
	file2 = _get_test_data_path("file2_nest.yml")

	expected_output = _read_test_file(f"expected_{format_name}_nest.txt")

	# Act
	actual_output = generate_diff(file1, file2, format_name)

	# Assert
	assert actual_output == expected_output


# Case 5: Comparing two flat .yaml files
@parametrize_output_formats
def test_generate_diff_flat_yaml(format_name) -> None:
	# Arrange
	file1 = _get_test_data_path("file1_flat.yaml")
	file2 = _get_test_data_path("file2_flat.yaml")

	expected_output = _read_test_file(f"expected_{format_name}_flat.txt")

	# Act
	actual_output = generate_diff(file1, file2, format_name)

	# Assert
	assert actual_output == expected_output


# Case 6: Comparing two nested .yaml files
@parametrize_output_formats
def test_generate_diff_nest_yaml(format_name) -> None:
	# Arrange
	file1 = _get_test_data_path("file1_nest.yaml")
	file2 = _get_test_data_path("file2_nest.yaml")

	expected_output = _read_test_file(f"expected_{format_name}_nest.txt")

	# Act
	actual_output = generate_diff(file1, file2, format_name)

	# Assert
	assert actual_output == expected_output


# Case 7: Selecting an unsupported formatter
def test_generate_diff_unsupported_formatter() -> None:
	# Arrange
	file1 = _get_test_data_path("file1_flat.json")
	file2 = _get_test_data_path("file2_flat.json")

	expected_output = "Unknown formatter: json. Available formatters: stylish, plain."

	# Act
	with pytest.raises(ValueError, match = re.escape(expected_output)):
		generate_diff(file1, file2, format_name = "json")


# Case 8: Comparing one supported file format and one unsupported file format
def test_generate_diff_unsupported_ext() -> None:
	# Arrange
	file1 = _get_test_data_path("file1_flat.json")
	file2 = _get_test_data_path("unsupported_file_type.txt")

	# Act & Assert
	with pytest.raises(ValueError, match="Unsupported file format"):
		generate_diff(file1, file2)
