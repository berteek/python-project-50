from gendiff.cli import get_arguments
from gendiff.cli import get_file_path1, get_file_path2, get_format
from gendiff.cli import log
from gendiff.diff import generate_diff


def run() -> None:
    args = get_arguments()
    file_path1 = get_file_path1(args)
    file_path2 = get_file_path2(args)
    format = get_format(args)
    diff = generate_diff(file_path1, file_path2, format)
    log(diff)


if __name__ == '__main__':
    run()
