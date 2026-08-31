"""Unit tests for the Parser Module (parser.py).

This module validates read_file(), which detects files of .json or .yml / .yaml type, reads them and
parses them into Python dictionaries. It also raises a ValueError if an unsupported file format is
passed to the function.

The tests cover seven cases:
Case 1: The functionn correctly detects a flat .json file, reads and parses it into a Python dictionary;
Case 2: The functionn correctly detects a nested .json file, reads and parses it into a Python dictionary;
Case 3: The function correctly detects a flat .yml file, reads and parses it into a Python dictionary;
Case 4: The function correctly detects a nested .yml file, reads and parses it into a Python dictionary;
Case 5: The function correctly detects a flat .yaml file, reads and parses it into a Python dictionary;
Case 6: The function correctly detects a nested .yaml file, reads and parses it into a Python dictionary;
Case 7: The function raises a ValueError in case of an unsupported file format.
"""


from gendiff.parser import read_file
from pathlib import Path
from .helpers import _get_test_data_path, _read_test_file
import pytest
import ast


# Case 1: flat .json files
def test_read_file_flat_json():
	# Arrange
	json_input_file = _get_test_data_path("file1_flat.json")
	expected_output_file = _get_test_data_path("expected_dict_output_flat.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(json_input_file)

	# Assert
	assert actual_output == expected_output


# Case 2: nested .json files
def test_read_file_nest_json():
	# Arrange
	json_input_file = _get_test_data_path("file1_nest.json")
	expected_output_file = _get_test_data_path("expected_dict_output_nest.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(json_input_file)

	# Assert
	assert actual_output == expected_output


# Case 3: flat .yml files
def test_read_file_flat_yml():
	# Arrange
	yml_input_file = _get_test_data_path("file1_flat.yml")
	expected_output_file = _get_test_data_path("expected_dict_output_flat.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(yml_input_file)

	# Assert
	assert actual_output == expected_output


# Case 4: nested .yml files
def test_read_file_nest_yml():
	# Arrange
	yml_input_file = _get_test_data_path("file1_nest.yml")
	expected_output_file = _get_test_data_path("expected_dict_output_nest.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(yml_input_file)

	# Assert
	assert actual_output == expected_output


# Case 5: flat .yaml files
def test_read_file_flat_yaml():
	# Arrange
	yaml_input_file = _get_test_data_path("file1_flat.yaml")
	expected_output_file = _get_test_data_path("expected_dict_output_flat.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(yaml_input_file)

	# Assert
	assert actual_output == expected_output


# Case 6: nested .yaml files
def test_read_file_nest_yaml():
	# Arrange
	yaml_input_file = _get_test_data_path("file1_nest.yaml")
	expected_output_file = _get_test_data_path("expected_dict_output_nest.txt")
	expected_output = ast.literal_eval(_read_test_file(expected_output_file))

	# Act
	actual_output = read_file(yaml_input_file)

	# Assert
	assert actual_output == expected_output


# Case 7: Unsupported files
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
