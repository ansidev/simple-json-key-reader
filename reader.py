import glob
import json
import os


def print_json_key(json_object, parent_key=None):
    if json_object is None:
        pass
    elif isinstance(json_object, (bool, int, float, str)):
        pass
    elif isinstance(json_object, (tuple, list)):
        for item in json_object:
            object_index = json_object.index(item)
            if parent_key is None:
                parent_key = ""
            sub_parent_key = parent_key + "[" + str(object_index) + "]"
            print_json_key(item, sub_parent_key)
    elif isinstance(json_object, dict):
        for key, value in json_object.items():
            output_key = key
            if parent_key is not None:
                output_key = parent_key + "." + key
            print(output_key)
            print_json_key(value, output_key)
        pass


def main():
    path = os.getcwd() + '/input/*.json'
    files = glob.glob(path)

    for file in files:
        print(file)
        f = open(file, 'r')
        jsonObject = json.load(f)
        print_json_key(jsonObject)
        print("\n")
        f.close()


if __name__ == '__main__':
    main()
