""" Difference Generator Module (diff_logic.py) for comparing configuration files.

This module contains the function generate_diff() that compares two structured
configuration files and outputs their differences in a user-selected
format.

Basically, generate_diff() is a composite function that wraps around four functions,
which form a pipeline:
1) read_file() => in parser.py -> reads two config files of .json or .yml / .yaml format and parses them into Python dictionaries;
2) build_diff() => in diff_builder.py -> compares two input dicts and generates a diff tree - a list of dictionary nodes;
3) format_stylish() => in formatter_stylish.py -> generates a user-friendly 'stylish' string representation of the differences;
4) format_plain() => in formatter_plain.py -> generates a user-friendly 'plain' string representation of the differences.
"""


from .diff_builder import build_diff
from .formatters.formatter_plain import format_plain
from .formatters.formatter_stylish import format_stylish
from .parser import read_file


def generate_diff(file_path_1: str, file_path_2: str, format_name='stylish') -> str:
	"""
	Read two files, compare their contents and return a user-selected output of their differences.

	Args:
		file_path_1 (str): The path to the first file to be read.
		file_path_2 (str): The path to the second file to be read.
		format_name (str): Specifies the formatter to be used for generating the output.

	Returns:
		tree-like output (str): Changes are indicated with - (removed), + (added), and "  " (unchanged).
		a flat list of sentences (str): each sentence describes a single changed property.
	"""
	# Format type mapper
	formatters = {"stylish": format_stylish, "plain": format_plain}

	# Allowed formats
	available_formats = ", ".join(formatters.keys())

	# Check if selected format is allowed
	if format_name not in formatters:
		raise ValueError(f"Unknown formatter: {format_name}. Available formatters: {available_formats}.")

	# Read the input files
	dict1 = read_file(file_path_1)
	dict2 = read_file(file_path_2)

	# Build a comparison internal representation (IR)
	diff_tree_ir = build_diff(dict1, dict2)

	# Format the output string
	diff_str = formatters[format_name](diff_tree_ir)

	return diff_str
