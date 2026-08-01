"""Parsing module for reading and parsing files of different formats.

This module detects files of .json or .yml / .yaml type, reads them and
parses them into Python dictionaries. It also handles errors, if it detects
unsupported file formats.
"""

import json


def read_file(file_path: str) -> dict:
	"""
	Read a JSON file and return its parsed contents as a Python object.

	Args:
		file_path (str): The path to the JSON file to be read.
	Returns:
		Python object (dict): The parsed JSON data is a dictionary.
	"""
	with open(file_path) as f:
		return json.load(f)
