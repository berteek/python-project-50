import argparse


def make_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    return parser


def add_arguments(parser):
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output'
    )


def parse_args(parser):
    args = parser.parse_args()
    return args


def run():
    parser = make_parser()
    add_arguments(parser)
    args = parse_args(parser)

    print(args.first_file, args.second_file)
