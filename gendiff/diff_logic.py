""" Difference Generator Module (diff_logic.py) for compring configuration files.

This module contains the function generate_diff() that compares two structured
configuration files and reports their differences in a user-selected
format.

It also contains helper functions used by generate_diff().
"""


from typing import Any

from .parser import read_file


def _get_sorted_keys(dict1: dict, dict2: dict) -> list:
	"""
	Extract dictionary keys and return a sorted list of unique keys.

	Args:
		dict1: dictionary 1
		dict2: dictionary 2
	Returns:
		sorted_keys: a sorted list of the unique keys from dict1 and dict2
	"""
	sorted_keys = sorted(list(dict1.keys() | dict2.keys()))
	return sorted_keys


def _format_value(value: Any) -> str:
	"""
	Determine the data type of input values and convert them to strings.

	Args:
		value: Any Python data type object.
	Returns:
		string: All input values are converted to strings.
	"""
	match value:
		case bool():
			return str(value).lower()
		case int():
			return str(value)
		case float():
			return str(value)
		case None:
			return "null"
		case _:
			return value


def generate_diff(file_path_1: str, file_path_2: str) -> str:
	"""
	Read two files, compare their contents and return a tree-like output.

	Args:
		file_path_1 (str): The path to the first file to be read.
		file_path_2 (str): The path to the second file to be read.

	Returns:
		tree-like output (str): Changes are indicated with - (removed), + (added), and "  " (unchanged).

	"""

	dict1 = read_file(file_path_1)
	dict2 = read_file(file_path_2)

	sorted_keys = _get_sorted_keys(dict1, dict2)

	output_str = ""

	for key in sorted_keys:

		value1 = dict1.get(key)
		value2 = dict2.get(key)

		if key in dict1 and key in dict2:
			if dict1.get(key) != dict2.get(key):
				output_str += f"  - {key}: {_format_value(value1)}\n  + {key}: {_format_value(value2)}\n"
			else:
				output_str += f"    {key}: {_format_value(value1)}\n"
		elif key in dict1:
			output_str += f"  - {key}: {_format_value(value1)}\n"
		elif key in dict2:
			output_str += f"  + {key}: {_format_value(value2)}\n"

	return f"{{\n{output_str}}}"
