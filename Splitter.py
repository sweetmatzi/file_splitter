#!/usr/bin/python

import sys
import glob
from shutil import copy


def main():
    jpgdestination="//Users/ich/Desktop/pyton/file_splitter-master/jpg"
    cr2destination="//Users/ich/Desktop/pyton/file_splitter-master/cr2"
    movdestination="//Users/ich/Desktop/pyton/file_splitter-master/mov"
    source="/Volumes/EOS_DIGITAL/DCIM/100CANON"
    for arg in sys.argv[0:]:
        print(arg)

    print(source)

    for path in glob.iglob(source+"/*.jpg"):
        print(path)
        copy(path, cr2destination)
    for path in glob.iglob(source+"/*.cr2"):
        print(path)
        copy(path, cr2destination)
    for path in glob.iglob(source+"/*.MOV"):
        print(path)
        copy(path, movdestination)


if __name__== "__main__":
  main()
