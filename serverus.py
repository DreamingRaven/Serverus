#!/usr/bin/env python3

# @Author: George Onoufriou <georgeraven>
# @Date:   2018-11-04
# @Filename: serverus.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-11-04
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou



import os, sys
from src.argz import argz
from src.helpers import placeholder



def main(args):
    print("HELLO WORLD")
    placeholder()



if __name__ == "__main__":
    description=None
    args = argz(sys.argv[1:], description=description)
    main(args=args)
