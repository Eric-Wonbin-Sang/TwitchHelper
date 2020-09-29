import os
import json


def get_curr_parent_dir():
    return os.path.dirname(os.getcwd()).replace("\\", "/")


def parse_json(json_path):
    if not os.path.exists(json_path):
        raise FileExistsError
    with open(json_path) as f:
        return json.load(f)
