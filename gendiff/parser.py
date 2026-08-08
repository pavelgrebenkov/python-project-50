"""Parser Module (parser.py) for reading and parsing files of different formats.

This module detects files of .json or .yml / .yaml type, reads them and
parses them into Python dictionaries. It also handles errors, if it detects
unsupported file formats.
"""

import json
from pathlib import Path

import yaml


def read_file(file_path: str) -> dict:
	"""
	Read a JSON or YAML file and return its parsed contents as a Python object.

	Args:
		file_path (str): The path to the JSON or YAML file to be read.
	Returns:
		Python object: The parsed JSON or YAML data is a dictionary.
		Error: In case of an unsupported file format, raise ValueError.
	"""
	# Get file extension
	file_ext = Path(file_path).suffix.lower()

	# Check if file ext is allowed
	if file_ext not in ['.json', '.yaml', '.yml']:
		raise ValueError(f"Unsupported file format {file_ext}. Only JSON and YAML allowed.")

	# Check if file is JSON or YAML
	with Path(file_path).open() as f:
		if file_ext == ".json":
			return json.load(f)
		return yaml.safe_load(f)
