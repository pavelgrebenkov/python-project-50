""" Difference Generator Module (diff_logic.py) for compring configuration files.

This module contains the function generate_diff() that compares two structured
configuration files and outputs their differences in a user-selected
format.

Baically, generate_diff() is a composite function that wraps around three functions,
which form a pipeline:
1) _read_file() => in parser.py -> reads two config files of .json or .yml / .yaml format and parses them into Python dictionaries;
2) build_diff() => in diff_builder.py -> compares two input dicts and generates a diff tree - a list of dictionary nodes;
3) format_stylish() => in formatter_stylish.py -> generates a user-friendly 'sytlish' string representation of the differences
between the two config files initially read by _read_file().
"""


from .diff_builder import build_diff
from .formatters.formatter_stylish import format_stylish
from .parser import read_file


def generate_diff(file_path_1: str, file_path_2: str, format_name='stylish') -> str:
	"""
	Read two files, compare their contents and return a tree-like output.

	Args:
		file_path_1 (str): The path to the first file to be read.
		file_path_2 (str): The path to the second file to be read.

	Returns:
		tree-like output (str): Changes are indicated with - (removed), + (added), and "  " (unchanged).

	"""
	# Read the input files
	dict1 = read_file(file_path_1)
	dict2 = read_file(file_path_2)

	# Build a comparison internal representation (IR)
	diff_tree_ir = build_diff(dict1, dict2)

	# Format the output string
	diff_str = format_stylish(diff_tree_ir)

	return diff_str
