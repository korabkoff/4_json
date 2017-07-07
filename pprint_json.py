import json
import sys
import os


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=None))


if __name__ == '__main__':
    json_content = load_json_data(sys.argv[1])
    pretty_print_json(json_content)
