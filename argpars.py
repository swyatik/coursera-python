import os
import tempfile
import argparse
import json


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('key', help='Input key', default=None)
    parser.add_argument('value', nargs='?', help='input value', default=None)
    return parser


def write_json_file(key, value):
    try:
        data = json.load(open(os.path.join(tempfile.gettempdir(), 'storage.data'), 'r'))
    except:
        data = {}
    if len(data) == 0:
        data[key] = [value]
        with open(os.path.join(tempfile.gettempdir(), 'storage.data'), 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        if key in data:
            values = data[key]
            values.append(value)
            del data[key]
            data[key] = values
        else:
            data[key] = [value]

        with open(os.path.join(tempfile.gettempdir(), 'storage.data'), 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def out_value_if_only_key(key):
    value_out = ''
    try:
        data = json.load(open(os.path.join(tempfile.gettempdir(), 'storage.data'), 'r'))
        if key in data:
            if len(data[key]) == 1:
                value_out = data[key][0]
            else:
                value_out = ', '.join(map(str, data[key]))
        else:
            value_out = None
    except:
        value_out = None

    return value_out


def main():
    parser = createParser()
    date_json = parser.parse_args()
    key = date_json.key
    value = date_json.value
    # out results
    if value == None:
        print(out_value_if_only_key(key))
    else:
        write_json_file(key, value)


if __name__ == '__main__':
    main()