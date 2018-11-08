# @Author: George Onoufriou <archer>
# @Date:   2018-11-08
# @Filename: argZ.py
# @Last modified by:   archer
# @Last modified time: 2018-11-08
# @License: Please see LICENSE file in project root
import os, sys
from collections.abc import MutableMapping # abstract base classes (abc)

class DictUtil(MutableMapping):

    def __init__(self, dictz=None):
        self.dict = dictz is not None else {}

    def __getitem__(self, key):
        print(key)
        self.dict[key]

    def __setitem__(self):
        None

    def __delitem__(self):
        None

    def __iter__(self):
        None

    def __len__(self):
        None

if(__name__ == "__main__"):

    dictz = {
        "flower": "buttercup",
        "jimmy": 69,
        "dingDong": "theWitchIsDead",
    }

    
