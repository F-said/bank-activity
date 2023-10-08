"""
A validation script to check if your data-engineering pipeline is operating as
intended.

To test the first part of your code, run:

python 04validate.py pt1

To test the first two parts of your pipeline, run:

python 04validate.py pt2

To test all the three parts of your pipeline, run:

python 04validate.py pt3

while in the code folder to test the completeness of your code.

The terminal output will tell you if your pipeline is successful.
"""
import sys
import os

from code.eng.01clean import Cleaner
from code.eng.02dummy import Dummify
from code.eng.03eng import Transformer

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pt1():
    df = Cleaner()
    return df


def pt2():
    pt1()
    pass


def pt3():
    pt1()
    pt2()
    pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{bcolors.FAIL}Error: Missing part of project to run.\
               \nUsage: python validate.py pt[1|2|3]{bcolors.ENDC}")

    if sys.argv[1] == "pt1":
        pt1()
    elif sys.argv[1] == "pt2":
        pt2()
    elif sys.argv[1] == "pt3":
        pt3()
