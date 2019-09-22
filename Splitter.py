#!/usr/bin/python

import sys
import glob

def main():
    for arg in sys.argv[0:]:
        print(arg)
    for path in glob.iglob("/tmp/*.xlsx"):
        print(path)

if __name__== "__main__":
  main()
