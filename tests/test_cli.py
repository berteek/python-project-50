import gendiff.cli as cli
import pytest


@pytest.fixture
def arguments():
    return {'file_path1': 'me', 'file_path2': 'you', 'format': 'standart'}


def test_make_arguments(arguments):
    assert arguments == cli.make_arguments('me', 'you')
    arguments['format'] = 'fancy'
    assert arguments == cli.make_arguments('me', 'you', format='fancy')


def test_get_file_path1(arguments):
    assert 'me' == cli.get_file_path1(arguments)


def test_get_file_path2(arguments):
    assert 'you' == cli.get_file_path2(arguments)


def test_get_format(arguments):
    assert 'standart' == cli.get_format(arguments)
    arguments['format'] = 'fancy'
    assert 'fancy' == cli.get_format(arguments)
