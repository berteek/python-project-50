from gendiff.diff import generate_diff


def test_generate_diff():
    expected = open('./tests/fixtures/json/expected1.txt').read().rstrip('\n')
    actual = generate_diff('./tests/fixtures/json/file1.json', './tests/fixtures/json/file2.json')
    assert expected == actual
