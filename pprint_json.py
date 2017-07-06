import json, sys


def load_data(filepath):
    with open(filepath, 'r') as handle:
        return json.load(handle)



def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=None))


if __name__ == '__main__':
    # print(sys.argv[1])
    data = load_data(sys.argv[1])
    pretty_print_json(data)
