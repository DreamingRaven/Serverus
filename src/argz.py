# @Author: George Onoufriou <georgeraven>
# @Date:   2018-11-04
# @Filename: argz.py
# @Last modified by:   georgeraven
# @Last modified time: 2018-11-04
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou

import argparse, configparser

def argz(argv=None, description=None):
    # creating parser object with description
    description = description if description is not None else "Serverus generalised python server"
    parser = argparse.ArgumentParser(description=description)

    # creating argument groups
    optional = parser._action_groups.pop() # popping -h off
    required = parser.add_argument_group('required arguments')

    # adding optional params at end again
    parser._action_groups.append(optional) # pushing -h back on with extras
    return vars(parser.parse_args(argv))
