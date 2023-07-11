#!/usr/bin/python3
"""2-append_write : append_write()"""


def append_write(filename="", text=""):
    """Opens a file and appends text to it"""
    with open(filename, 'a', encoding="utf-8") as af:
        return(af.write(text))
