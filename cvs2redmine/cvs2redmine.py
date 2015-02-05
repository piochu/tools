#!/usr/bin/python3
__author__ = 'piochu'
import argparse
import os.path
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="csv file")
    parser.add_argument("-d", help="custom delimiter (by default semicolon)", default=";")
    parser.add_argument("-n", help="disable table header", action="store_true")
    
    args = parser.parse_args()

    input = args.file

    if not os.path.isfile(input):
        print("File %s don't exist." % input)
        sys.exit(1)

    data = open(input)

    for i, line in enumerate(data):
        columns = line.split(args.d)

        if i and not args.n:
            for item in columns:
                print("|%s" % item.strip(), end="")

        if not i or args.n:
            for item in columns:
                print("|_.%s" % item.strip(), end="")
        print("|")

    data.close()

if __name__ == "__main__":
    main()