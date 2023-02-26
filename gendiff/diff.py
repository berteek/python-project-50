import json
from functools import reduce


def generate_diff(
        file_path1: str,
        file_path2: str,
        format: str="standart"
    ) -> str:

    file1 = open(file_path1)
    file2 = open(file_path2)

    json1 = json.load(file1)
    json2 = json.load(file2)

    file1.close()
    file2.close()
    
    removed_keys = set(json1.keys()).difference(set(json2.keys()))
    removed = {key: json1[key] for key in removed_keys}

    same = []
    for key in json2:
        if key in json1:
            if json1[key] == json2[key]:
                same.append((key, json1[key]))

    updated = []
    for key in json2:
        if key in json1:
            if json1[key] != json2[key]:
                updated.append((key, json1[key], json2[key]))
    
    added_keys = set(json2.keys()).difference(set(json1.keys()))
    added = {key: json2[key] for key in added_keys}

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
        lambda acc, pair: acc + f'\t- {pair[0]}: {pair[1]}\n\t+ {pair[0]}: {pair[2]}\n',
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
