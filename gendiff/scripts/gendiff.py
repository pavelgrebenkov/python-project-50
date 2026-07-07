import argparse
import json


def _read_json(file_path):
	with open(file_path) as f:
		return json.load(f)


def main():
	parser = argparse.ArgumentParser(prog="gendiff", description="Compares two configuration files and shows a difference.")

	parser.add_argument("first_file")
	parser.add_argument("second_file")
	parser.add_argument("-f", "--format", help="set format of output", default="stylish")

	args = parser.parse_args()

	data_1 = _read_json(args.first_file)
	data_2 = _read_json(args.second_file)

	print(data_1)
	print(data_2)


if __name__ == "__main__":
    main()
