#!/usr/bin/env python3

# @Author: George Onoufriou <georgeraven>
# @Date:   2018-11-04
# @Filename: serverus.py
# @Last modified by:   archer
# @Last modified time: 2018-11-05
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou



import os, sys
from src.argz import argz
from src.serverz import serverz
from src.helperz import placeholder



def main(args):

    srv = serverz()

    if(args["toStartServer"] == True):
        print("starting server...")
        srv.start()
    else:
        print("skipping server start sequence")

    if(args["toStopServer"] == True):
        print("stopping server...")
        srv.stop()



if __name__ == "__main__":
    description=None
    args = argz(sys.argv[1:], description=description)
    main(args=args)
