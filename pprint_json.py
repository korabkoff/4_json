import json
import sys
import os


def get_commandline_arg(index):
    if len(sys.argv) == index+1:
        return sys.argv[index]
    else:
        return None


def load_json_data(file_path):

    if not file_path:
        return None
    elif not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as json_file:
        if not json_file.read(1):  # in case of empty file
            return None

        json_file.seek(0)  # Return to the start of content
        return json.load(json_file)


def pretty_print_json(data):
    if not data:
        return None

    return json.dumps(data, ensure_ascii=False, indent=4, sort_keys=None)


if __name__ == '__main__':

    json_file_path = get_commandline_arg(1)

    json_content = load_json_data(json_file_path)

    print(pretty_print_json(json_content))
