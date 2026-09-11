"""
The Difference Builder Module (diff_builder.py):

This module contains the function build_diff() that compares two Python
dictionaries and builds an abstract difference tree - i.e. an internal representation
(IR) of the differences between the inputs. For each dictionary key, the IR captures

- its status: added, removed, updated, unchanged, or nested.
- its old value (if applicable), new value (if applicable), and children (if nested).
"""


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


def build_diff(dict1: dict, dict2: dict) -> list:
	"""
	Compare two dictionaries and return a list of dictionaries, where each dictionary is a node in a diff tree.

	Args:
		dict1: dictionary 1
		dict2: dictionary 2

	Returns:
		list_of_nodes: an internal representation (IR) of the differences between dict1 and dict2 
	"""

	sorted_keys = _get_sorted_keys(dict1, dict2)

	list_of_nodes = []

	for key in sorted_keys:

		node = {}

		value1 = dict1.get(key)
		value2 = dict2.get(key)

		if key not in dict2:
			node['key'] = key
			node['status'] = 'removed'
			node['old_value'] = value1
			node['new_value'] = None
			node['children'] = None

		elif key not in dict1:
			node['key'] = key
			node['status'] = 'added'
			node['old_value'] = None
			node['new_value'] = value2
			node['children'] = None

		elif key in dict1 and key in dict2:
			if isinstance(value1, dict) and isinstance(value2, dict):
				node['key'] = key
				node['status'] = 'nested'
				node['old_value'] = None
				node['new_value'] = None
				node['children'] = build_diff(value1, value2)

			elif value1 == value2:
				node['key'] = key
				node['status'] = 'unchanged'
				node['old_value'] = value1
				node['new_value'] = value1
				node['children'] = None

			elif value1 != value2:
				node['key'] = key
				node['status'] = 'updated'
				node['old_value'] = value1
				node['new_value'] = value2
				node['children'] = None

		list_of_nodes.append(node)

	return list_of_nodes
