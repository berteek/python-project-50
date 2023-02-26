import argparse


def make_arguments(file_path1: str, file_path2: str, format: str='standart') -> dict[str, str]:
    return {
        'file_path1': file_path1,
        'file_path2': file_path2,
        'format': format
    }


def get_file_path1(args: dict[str, str]) -> str:
    return args['file_path1']


def get_file_path2(args: dict[str, str]) -> str:
    return args['file_path2']


def get_format(args: dict[str, str]) -> str:
    return args['format']


def log(message: str) -> None:
    print(message)


def get_arguments() -> dict[str, str]:
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
    )
    args = parser.parse_args()
    return make_arguments(args.first_file, args.second_file, args.format)
