#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "tjhindman"


import sys
import argparse


def upper(text):
    up = text.upper()
    return up


def lower(text):
    low = text.lower()
    return low


def title(text):
    title = text.title()
    return title


def create_parser():
    """Creates and returns an argparse cmd line option parser"""

    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument("-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument("-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument("-t", "--title", help="convert text to titlecase", action="store_true")

    return parser


def main(args):
    """Implementation of echo"""

    arg_check = create_parser()

    if not args:
        arg_check.print_usage()
        sys.exit()

    args = arg_check.parse_args(args)

    if args.upper:
        upper(args.text)
    if args.lower:
        lower(args.text)
    if args.title:
        title(args.text)



if __name__ == '__main__':
    main(sys.argv[1:])
