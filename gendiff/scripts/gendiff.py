import argparse

from gendiff.diff_logic import generate_diff


def main():
	parser = argparse.ArgumentParser(prog="gendiff", description="Compares two configuration files and shows a difference.")

	parser.add_argument("first_file")
	parser.add_argument("second_file")
	parser.add_argument("-f", "--format", help="set format of output", default="stylish")

	args = parser.parse_args()

	diff_string = generate_diff(args.first_file, args.second_file)

	print(diff_string)


if __name__ == "__main__":
    main()
