#!/usr/bin/python

import sys
import glob
from shutil import copy


def main():
    rawdestination="/tmp/raw"
    pngdestination="/tmp/png"
    for arg in sys.argv[0:]:
        print(arg)



    for path in glob.iglob("/tmp/*.raw"):
        print(path)
        copy(path, rawdestination)
    for path in glob.iglob("/tmp/*.png"):
        print(path)
        copy(path, pngdestination)


if __name__== "__main__":
  main()
