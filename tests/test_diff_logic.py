from gendiff.diff_logic import generate_diff
from pathlib import Path


def _get_test_data_path(filename):
	path = Path(__file__).parent / "test_data" / filename
	return path


def _read_test_file(filename):
	return _get_test_data_path(filename).read_text().strip()


# Case 1: Both files identical → output shows keys without - or +.
def test_generate_diff_unchanged_key(mocker):
	# Arrange
	file1 = {"host": "hexlet.io"}
	file2 = {"host": "hexlet.io"}
	expected_output = "{\n    host: hexlet.io\n}"

	mock_read = mocker.patch("gendiff.diff_logic._read_file")
	mock_read.side_effect = [file1, file2]

        # Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# Case 2: Keys added only in second file → output shows keys with +.
def test_generate_diff_add_key(mocker):
	# Arrange
	file1 = {}
	file2 = {"host": "hexlet.io"}
	expected_output = "{\n  + host: hexlet.io\n}"

	mock_read = mocker.patch("gendiff.diff_logic._read_file")
	mock_read.side_effect = [file1, file2]

	# Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# Case 3: Keys removed in second file → output shows keys with -.
def test_generate_diff_remove_key(mocker):
	# Arrange
	file1 = {"host": "hexlet.io"}
	file2 = {}
	expected_output = "{\n  - host: hexlet.io\n}"

	mock_read = mocker.patch("gendiff.diff_logic._read_file")
	mock_read.side_effect = [file1, file2]

	# Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# Case 4: Keys updated (values differ) → output shows keys with - then +.
def test_generate_diff_update_key(mocker):
	# Arrange
	file1 = {"host": "hexlet.io"}
	file2 = {"host": "hexlet.com"}
	expected_output = "{\n  - host: hexlet.io\n  + host: hexlet.com\n}"

	mock_read = mocker.patch("gendiff.diff_logic._read_file")
	mock_read.side_effect = [file1, file2]

	# Act
	actual_output = generate_diff("file1_path", "file2_path")

	# Assert
	assert actual_output == expected_output


# Case 5: Mixed changes (all of the above combined)
def test_generate_diff_overall():
	# Arrange
	file1 = _get_test_data_path("file1.json")
	file2 = _get_test_data_path("file2.json")
	expected_output = _read_test_file("expected_stylish.txt")

	# Act
	actual_output = generate_diff(file1, file2)

	# Assert
	assert actual_output == expected_output
