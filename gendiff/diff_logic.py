import json
from typing import Any


def _read_file(file_path: str) -> dict:
	"""
	Read a JSON file and return its parsed contents as a Python object.

	Args:
		file_path (str): The path to the JSON file to be read.
	Returns:
		Python object (dict): The parsed JSON data.
	"""
	with open(file_path) as f:
		return json.load(f)


def _get_sorted_keys(dict1: dict, dict2: dict) -> list:
	"""
	Extract dictionary keys and return a sorted list of unique keys.

	Args:
		dict1 (dict): dictionary 1
		dict2 (dict): dictionary 2
	Returns:
		sorted_keys (list): a sorted list of the unique keys from dict1 and dict2
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


def generate_diff(file1_path: str, file2_path: str) -> str:
	"""
	Read two files, compare their contents and return a tree-like output.

	Args:
		file1_path (str): The path to the first file to be read.
		file2_path (str): The path to the second file to be read.

	Returns:
		tree-like output (str): Changes are indicated with - (removed), + (added), and empty space (unchanged).

	"""
	dict1 = _read_file(file1_path)
	dict2 = _read_file(file2_path)

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
