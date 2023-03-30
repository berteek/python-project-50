from gendiff.diff import generate_diff
import pytest


@pytest.fixture
def diff():
    return open('./tests/fixtures/expected1.txt').read().rstrip('\n')


def test_works_with_json(diff):
    expected = diff
    actual = generate_diff('./tests/fixtures/json/file1.json', './tests/fixtures/json/file2.json')
    assert expected == actual


def test_works_with_yaml(diff):
    expected = diff
    actual = generate_diff('./tests/fixtures/yaml/file1.yml', './tests/fixtures/yaml/file2.yaml')
    assert expected == actual


def test_works_with_mixed(diff):
    expected = diff
    actual = generate_diff('./tests/fixtures/json/file1.json', './tests/fixtures/yaml/file2.yaml')
    assert expected == actual
