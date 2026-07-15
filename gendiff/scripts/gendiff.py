"""
Gendiff Entry Point Module.
This module provides a command-line interface (CLI) to compare two configuration
files and output the differences in various formats.
"""

import argparse

from gendiff.diff_logic import generate_diff


def main():
	"""
	Execute the core command-line application.

	Parses command-line arguments for two configuration files, calculates
	their difference using gendiff's logic, and prints the result to stdout.

	Command-line Arguments:
		first_file (str): Path to the first configuration file.
		second_file (str): Path to the second configuration file.
		-f, --format (str): The output format (default is 'stylish').
	"""
	parser = argparse.ArgumentParser(prog="gendiff", description="Compares two configuration files and shows a difference.")

	parser.add_argument("first_file")
	parser.add_argument("second_file")
	parser.add_argument("-f", "--format", help="set format of output", default="stylish")

	args = parser.parse_args()

	diff_string = generate_diff(args.first_file, args.second_file)

	print(diff_string)


if __name__ == "__main__":
    main()
