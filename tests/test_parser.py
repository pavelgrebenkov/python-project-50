"""Unit tests for the Parser Module (parser.py).

This module validates read_file(), which detects files of .json or .yml / .yaml type, reads them and 
parses them into Python dictionaries. It also raises a ValueError if an unsupported file format is
passed to the function.

The tests cover four cases:
Case 1: The functionn correctly detects a .json file, reads and parses it into a Python dictionary;
Case 2: The function correctly detects a .yml file, reads and parses it into a Python dictionary;
Case 2: The function correctly detects a .yaml file, reads and parses it into a Python dictionary;
Case 3: The function raises a ValueError in case of an unsupported file format.
"""

from gendiff.parser import read_file
from pathlib import Path
import pytest
import ast


def _get_test_data_path(filename: str) -> Path:
	path = Path(__file__).parent / "test_data" / filename
	return path


def _read_test_file(filename: str)-> str:
    return _get_test_data_path(filename).read_text().strip()


# Case 1: .json files
def test_read_file_json():
	# Arrange
	json_input_file = _get_test_data_path("file1.json")
	expected_output_file = _get_test_data_path("expected_dict_output.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(json_input_file)

	# Assert
	assert actual_output == expected_output


# Case 2: .yml files
def test_read_file_yml():
	# Arrange
	yml_input_file = _get_test_data_path("file1.yml")
	expected_output_file = _get_test_data_path("expected_dict_output.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(yml_input_file)

	# Assert
	assert actual_output == expected_output


# Case 3: .yaml files
def test_read_file_yaml():
	# Arrange
	yaml_input_file = _get_test_data_path("file1.yaml")
	expected_output_file = _get_test_data_path("expected_dict_output.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(yaml_input_file)

	# Assert
	assert actual_output == expected_output


# Case 4: Unsupported files
def test_read_file_unsupported_ext():
	# Arrange
	unsupported_input_file = _get_test_data_path("unsupported_file_type.txt")
	file_ext = Path("unsupported_file_type.txt").suffix.lower()
	expected_output = f"Unsupported file format {file_ext}. Only JSON and YAML allowed."

	# Act
	with pytest.raises(ValueError, match = expected_output):
		actual_output = read_file(unsupported_input_file)
		# Assert
		assert actual_output == expected_output
