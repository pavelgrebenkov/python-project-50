import json


def _read_file(file_path):
	with open(file_path) as f:
		return json.load(f)


def _get_sorted_keys(dict1, dict2):
	sorted_keys = sorted(list(dict1.keys() | dict2.keys()))
	return sorted_keys


def _format_value(value):
	match value:
		case bool():
			return str(value).lower()
		case int():
			return str(value)
		case None:
			return "null"
		case _:
			return value


def generate_diff(file1_path: str, file2_path: str) -> str:
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
