import json
import sys
import os
import argparse


def parse_args(args):

    parser = argparse.ArgumentParser(description='Pritty print for JSON')
    parser.add_argument('filepath', help='File path to JSON file', type=argparse.FileType('r'))

    return parser.parse_args(args)


def load_json_data(file_path):

    if not file_path or not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as json_file:
        try:
            return json.load(json_file)

        except AssertionError:
            print('Specified file is not a JSON type or empty')


def pretty_print_json(raw_json):

    if not raw_json:
        return None

    return json.dumps(raw_json, ensure_ascii=False, indent=4, sort_keys=None)


if __name__ == '__main__':

    try:
        parser = parse_args(sys.argv[1:])

        json_file_path = parser.filepath.name
    except:
        json_file_path = None

    if json_file_path:
        json_content = load_json_data(json_file_path)

        if json_content:
            print(pretty_print_json(json_content))
