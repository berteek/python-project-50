from gendiff.parsing import parse
from functools import reduce


def load_files(
        file_path1: str,
        file_path2: str) -> tuple[dict[str, str], dict[str, str]]:

    file1 = parse(file_path1)
    file2 = parse(file_path2)

    return file1, file2


def find_removed(
        json1: dict[str, str],
        json2: dict[str, str]) -> dict[str, str]:

    removed = {}
    for key in json1:
        if key not in json2:
            removed[key] = json1[key]
    return removed


def find_same(
        json1: dict[str, str],
        json2: dict[str, str]) -> list[tuple[str, str]]:

    same = []
    for key in json2:
        if key in json1 and json1[key] == json2[key]:
            same.append((key, json1[key]))
    return same


def find_updated(
        json1: dict[str, str],
        json2: dict[str, str]) -> list[tuple[str, str, str]]:
    updated = []
    for key in json2:
        if key in json1 and json1[key] != json2[key]:
            updated.append((key, json1[key], json2[key]))
    return updated


def find_added(
        json1: dict[str, str],
        json2: dict[str, str]) -> dict[str, str]:

    added_keys = set(json2.keys()).difference(set(json1.keys()))
    added = {key: json2[key] for key in added_keys}
    return added


def make_diff_string(
        removed: dict[str, str],
        same: list[tuple[str, str]],
        updated: list[tuple[str, str, str]],
        added: dict[str, str]) -> str:
    diff = '{\n'
    diff += reduce(
        lambda acc, pair: acc + f'\t- {pair[0]}: {pair[1]}\n',
        removed.items(),
        ''
    )
    diff += reduce(
        lambda acc, pair: acc + f'\t  {pair[0]}: {pair[1]}\n',
        same,
        ''
    )
    diff += reduce(
        lambda acc, pair: acc + (f'\t- {pair[0]}: {pair[1]}\n\t'
                                 f'+ {pair[0]}: {pair[2]}\n'),
        updated,
        ''
    )
    diff += reduce(
        lambda acc, pair: acc + f'\t+ {pair[0]}: {pair[1]}\n',
        added.items(),
        ''
    )
    diff += '}'
    return diff


def generate_diff(
        file_path1: str,
        file_path2: str,
        format: str = "standard") -> str:

    json1, json2 = load_files(file_path1, file_path2)

    removed = find_removed(json1, json2)
    same = find_same(json1, json2)
    updated = find_updated(json1, json2)
    added = find_added(json1, json2)

    diff = make_diff_string(removed, same, updated, added)

    return diff
