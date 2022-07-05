#!/usr/bin/python3
"""save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function writes an object to a text file using JSON rep"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
