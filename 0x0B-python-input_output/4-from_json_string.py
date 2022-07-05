#!/usr/bin/python3
""" from JSON string to object"""
import json

def from_json_string(my_str):
    """function returns an object repped by a JSON string"""
    return json.load(my_str)
