#!/usr/bin/python3
"""1-write_file : write_file()"""


def write_file(filename="", text=""):
    """Opens a file and writes into it"""
    with open(filename, 'w', encoding="UTF8") as write_file:
        return(write_file.write(text))
