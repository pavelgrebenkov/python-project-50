"""Unit tests for the Builder Module (diff_builder.py).

This module validates build_diff(), which takes two dictionaries, flat or nested, as input and generates
an internal representation (IR) difference tree. An IR is a list of dictionaries, where each dictionary
is a node that has the following keys and possible values:

- key: the name of a key from an input dictionary
- status: 'added' / 'removed' / 'updated' / 'unchanged' / 'nested'.
- old_value (optional): the value from the first input dictionary (for 'removed', 'updated').
- new_value (optional): the value from the second input dictionary (for 'added', 'updated').
- children (optional): a list of child nodes, only for 'nested' status.

The tests cover 12 cases - 6 cases for each type of dictionary, flat and nested. The tests cover
the following possible situations:
1. empty dictionaries
2. unchanged status
3. added status
4. removed status
5. updated status
6. mixed (2. - 5.)
"""


from gendiff.diff_builder import build_diff
from pathlib import Path
from .helpers import _get_test_data_path, _read_test_file
import pytest
import ast


# I. FLAT DICTIONARIES:
# Case 1: flat => empty dictionaries
def test_build_diff_empty_flat_dict():
	# Arrange:
	dict1 = {}
	dict2 = {}
	expected_output = []

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 2: flat => status: unchanged
def test_build_diff_flat_status_unchanged():
	# Arrange:
	dict1 = {"host": "hexlet.io"}
	dict2 = {"host": "hexlet.io"}
	expected_output = [{'key': 'host', 'status': 'unchanged', 'old_value': 'hexlet.io', 'new_value': 'hexlet.io', 'children': None}]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 3: flat => status: added
def test_build_diff_flat_status_added():
	# Arrange:
	dict1 = {}
	dict2 = {"host": "hexlet.io"}
	expected_output = [{'key': 'host', 'status': 'added', 'old_value': None, 'new_value': 'hexlet.io', 'children': None}]

	# Act
	actual_output = build_diff(dict1, dict2)

    	# Assert
	assert actual_output == expected_output


# Case 4: flat => status: removed
def test_build_diff_flat_status_removed():
	# Arrange:
	dict1 = {"host": "hexlet.io"}
	dict2 = {}
	expected_output = [{'key': 'host', 'status': 'removed', 'old_value': 'hexlet.io', 'new_value': None, 'children': None}]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 5: flat => status: updated
def test_build_diff_flat_status_updated():
	# Arrange:
	dict1 = {"host": "hexlet.io"}
	dict2 = {"host": "hexlet.com"}
	expected_output = [{'key': 'host', 'status': 'updated', 'old_value': 'hexlet.io', 'new_value': 'hexlet.com', 'children': None}]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 6: flat => integrated (cases 2 - 5)
def test_build_diff_flat_overall():
	# Arrange:
	dict1 = ast.literal_eval(_read_test_file(_get_test_data_path("expected_dict_output_flat1.txt")))
	dict2 = ast.literal_eval(_read_test_file(_get_test_data_path("expected_dict_output_flat2.txt")))
	expected_output = ast.literal_eval(_read_test_file(_get_test_data_path("expected_ir_flat.txt")))

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output




# II. NESTED DICTIONAREIES:
# Case 1: nested => empty dictionaries
def test_build_diff_empty_nest_dict():
	# Arrange
	dict1 = {"common": {}}
	dict2 = {"common": {}}
	expected_output = [
				{
					'key': 'common',
					'status': 'nested',
					'old_value': None,
					'new_value': None,
					'children': [] # Empty list
				}
			]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 2: nested => status: unchanged
def test_build_diff_nest_status_unchanged():
	# Arrange:
	dict1 = {"common": {"setting1": "Value 1"}}
	dict2 = {"common": {"setting1": "Value 1"}}
	expected_output = [
				{
					'key': 'common',
					'status': 'nested',
					'old_value': None,
					'new_value': None,
					'children': [{'key': 'setting1', 'status': 'unchanged', 'old_value': 'Value 1', 'new_value': 'Value 1', 'children': None}]
				}
			]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 3: nested => status: added
def test_build_diff_nest_status_added():
	# Arrange:
	dict1 = {"common": {}}
	dict2 = {"common": {"setting1": "Value 1"}}
	expected_output = [
				{
					'key': 'common',
					'status': 'nested',
					'old_value': None,
					'new_value': None,
					'children': [{'key': 'setting1', 'status': 'added', 'old_value': None, 'new_value': 'Value 1', 'children': None}]
				}
			]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 4: nested => status: removed
def test_build_diff_nest_status_removed():
	# Arrange:
	dict1 = {"common": {"setting1": "Value 1"}}
	dict2 = {"common": {}}
	expected_output = [
				{
					'key': 'common',
					'status': 'nested',
					'old_value': None,
					'new_value': None,
					'children': [{'key': 'setting1', 'status': 'removed', 'old_value': 'Value 1', 'new_value': None, 'children': None},]
				}
			]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 5: nested => status: updated
def test_build_diff_nest_status_updated():
	# Arrange:
	dict1 = {"common": {"setting1": "Value 1"}}
	dict2 = {"common": {"setting1": "Value 2"}}
	expected_output = [
				{
					'key': 'common',
					'status': 'nested',
					'old_value': None,
					'new_value': None,
					'children': [{'key': 'setting1', 'status': 'updated', 'old_value': 'Value 1', 'new_value': 'Value 2', 'children': None}]
				}
			]

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output


# Case 6: nested => all of the above (integrated)
def test_build_diff_nest_overall():
	# Arrange:
	dict1 = ast.literal_eval(_read_test_file(_get_test_data_path("expected_dict_output_nest1.txt")))
	dict2 = ast.literal_eval(_read_test_file(_get_test_data_path("expected_dict_output_nest2.txt")))
	expected_output = ast.literal_eval(_read_test_file(_get_test_data_path("expected_ir_nest.txt")))

	# Act
	actual_output = build_diff(dict1, dict2)

	# Assert
	assert actual_output == expected_output
