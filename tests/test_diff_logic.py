"""Unit and integrated tests for the Difference Generator Module (diff_logic.py).

This module validates generate_diff(), which compares two structured
configuration files and reports their differences in a user-selected format.

The unit tests cover four cases:
Case 1: Both input files are identical;
Case 2: New information is added to the second file;
Case 3: Information is removed from the second file;
Case 4: Information is updated in the second file.

The integrated tests cover three cases:
Case 1: Comparing two .json files;
Case 2: Comparing two .yml files;
Case 3: Comparing two .yaml files;
Case 4: Comparing one supported file format and one unsupported file format.

pytest-mock API:
	mocker: Mock the inputs to the helper function, read_file(),
	used inside generate_diff().
"""

import pytest
from gendiff.diff_logic import generate_diff
from pytest_mock import MockerFixture
from pathlib import Path
from .helpers import _get_test_data_path, _read_test_file


# UNIT TESTS
# Case 1: Both files identical → output shows keys without - or +.
def test_generate_diff_unchanged_key(mocker: MockerFixture) -> None:
	# Arrange
	file1 = {"host": "hexlet.io"}
	file2 = {"host": "hexlet.io"}
	expected_output = "{\n    host: hexlet.io\n}"

	mock_read = mocker.patch("gendiff.diff_logic.read_file")
	mock_read.side_effect = [file1, file2]

        # Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# Case 2: Keys added only in second file → output shows keys with +.
def test_generate_diff_add_key(mocker: MockerFixture) -> None:
	# Arrange
	file1 = {}
	file2 = {"host": "hexlet.io"}
	expected_output = "{\n  + host: hexlet.io\n}"

	mock_read = mocker.patch("gendiff.diff_logic.read_file")
	mock_read.side_effect = [file1, file2]

	# Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# Case 3: Keys removed in second file → output shows keys with -.
def test_generate_diff_remove_key(mocker: MockerFixture) -> None:
	# Arrange
	file1 = {"host": "hexlet.io"}
	file2 = {}
	expected_output = "{\n  - host: hexlet.io\n}"

	mock_read = mocker.patch("gendiff.diff_logic.read_file")
	mock_read.side_effect = [file1, file2]

	# Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# Case 4: Keys updated (values differ) → output shows keys with - then +.
def test_generate_diff_update_key(mocker: MockerFixture) -> None:
	# Arrange
	file1 = {"host": "hexlet.io"}
	file2 = {"host": "hexlet.com"}
	expected_output = "{\n  - host: hexlet.io\n  + host: hexlet.com\n}"

	mock_read = mocker.patch("gendiff.diff_logic.read_file")
	mock_read.side_effect = [file1, file2]

	# Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# INTEGRATED TESTS
# Case 1: Comparing two .json files
def test_generate_diff_json() -> None:
	# Arrange
	file1 = _get_test_data_path("file1.json")
	file2 = _get_test_data_path("file2.json")
	expected_output = _read_test_file("expected_stylish.txt")

	# Act
	actual_output = generate_diff(file1, file2)

	# Assert
	assert actual_output == expected_output


# Case 2: Comparing two .yml files
def test_generate_diff_yml() -> None:
	# Arrange
	file1 = _get_test_data_path("file1.yml")
	file2 = _get_test_data_path("file2.yml")
	expected_output = _read_test_file("expected_stylish.txt")

	# Act
	actual_output = generate_diff(file1, file2)

	# Assert
	assert actual_output == expected_output


# Case 3: Comparing two .yaml files
def test_generate_diff_yaml() -> None:
	# Arrange
	file1 = _get_test_data_path("file1.yaml")
	file2 = _get_test_data_path("file2.yaml")
	expected_output = _read_test_file("expected_stylish.txt")

	# Act
	actual_output = generate_diff(file1, file2)

	# Assert
	assert actual_output == expected_output


# Case 4: Comparing one supported file format and one unsupported file format
def test_generate_diff_unsupported_ext() -> None:
	# Arrange
	file1 = _get_test_data_path("file1.json")
	file2 = _get_test_data_path("unsupported_file_type.txt")

	# Act & Assert
	with pytest.raises(ValueError, match="Unsupported file format"):
		generate_diff(file1, file2)
