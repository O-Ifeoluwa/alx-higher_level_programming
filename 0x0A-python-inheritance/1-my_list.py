#!/usr/bin/python3
"""my list"""


class MyList(list):
    """MyList inherits from list...duh"""
    def print_sorted(self):
        """prints an ascending sorted list"""
        print(sorted(self))

