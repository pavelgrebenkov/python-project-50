"""Helper Module (conftest.py) for the testing modules (test_diff_logic.py, test_parser.py)"""


from pathlib import Path


def _get_test_data_path(filename: str) -> Path:
	path = Path(__file__).parent / "test_data" / filename
	return path


def _read_test_file(filename: str) -> str:
	return _get_test_data_path(filename).read_text().strip()
