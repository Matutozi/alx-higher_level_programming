#!/usr/bin/python3
"""Module name : 0-read_file, Method : read_file()"""


def read_file(filename=""):
    """Reads text file and print to stdout"""
    with open(filename, "r", encoding='UTF8') as read_file:
        print(read_file.read(), end="")
