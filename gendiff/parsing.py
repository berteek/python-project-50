import os
import json
import yaml


def parse(path: str) -> dict[str, str]:
    _, file_extension = os.path.splitext(path)
    file = open(path, 'r')
    result = {}
    match file_extension:
        case '.yml' | '.yaml':
            file_content = file.read()
            result = yaml.safe_load(file_content)
        case '.json':
            result = json.load(file)
        case _:
            raise ValueError('The file\'s format is not supported')
    file.close()
    return result
