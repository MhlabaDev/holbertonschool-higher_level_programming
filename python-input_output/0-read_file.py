#!/usr/bin/python3
"""a function that reads a text file (UTF8) and pirnts it to stdout"""


def read_file(filename=""):
    """read 'filename'"""

    with open(filename, "r", encoding='utf-8') as a_file:
        print("{}".format(a_file.read()), end="")
