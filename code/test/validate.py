"""
A validation script to check if your data-engineering pipeline is operating as
intended.

To test the first part of your code, run:

python -m code.test.validate pt1

To test the first two parts of your pipeline, run:

python -m code.test.validate pt2

To test all the three parts of your pipeline, run:

python -m code.test.validate pt3

while in the `code/test` folder to test the completeness of your code.

The terminal output will tell you if your pipeline is successful.
"""
import sys

from code.clean01 import Cleaner
from code.dummy02 import Dummify
from code.eng03 import Transformer

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def pt1():
    # Create Cleaner object
    data = Cleaner(r"data\raw\bank.csv")

    # try to clean data
    try:
        data.clean()
    except Exception as e:
        print(f"{FAIL}PT1 fails: exception occured: {e}{ENDC}")
        return 0

    # check if the balance type is float ($$$)
    if data.df.balance.dtype != "float":
        print(f"{FAIL}PT1 fails: Balance is not a float{ENDC}")
        return 0
    # check if we dropped unneeded columns
    if set(["day", "month"]).issubset(set(data.df.columns)):
        print(f"{FAIL}PT1 fails: Day, month, and duration columns still exist{ENDC}")
        return 0
    # check to see that our data sample is representative
    if data.df.balance.max() > 60_000:
        print(f"{FAIL}PT1 fails: Balance column still has values > 60,000{ENDC}")
        return 0

    # confirm to tester that all looks good!
    print(f"{OKGREEN}PT1 passes!{ENDC}")
    return 1


def pt2():
    # create Dummify object
    data = Dummify(r"data\raw\bank.csv")

    # try to run encode, and check if encoding was successful
    try:
        data.encode()
    except Exception as e:
        print(f"{FAIL}PT2 fails: exception occured: {e}{ENDC}")
        return 0

    if data.df.shape != (45211, 29):
        print(f"{FAIL}PT2 fails: 'job' & 'education' columns not properly encoded.{ENDC}")
        return 0

    # confirm to tester that all looks good!
    print(f"{OKGREEN}PT2 passes!{ENDC}")
    return 1


def pt3():
    # create Transformer
    data = Transformer(r"data\raw\bank.csv")

    # attempt to run transform method
    try:
        data.transform()
    except Exception as e:
        print(f"{FAIL}PT3 fails: exception occured: {e}{ENDC}")
        return 0

    # check if y was renamed
    if "purchase_term" not in data.df.columns or "y" in data.df.columns:
        print(f"{FAIL}PT3 fails: 'y' column has not been renamed.{ENDC}")
        return 0
    # check if duration_year column was created
    if "duration_year" not in data.df.columns:
        print(f"{FAIL}PT3 fails: 'duration_year' not created.{ENDC}")
        return 0
    # check if duration_year was calculated correctly
    if not data.df["duration_year"].equals(data.df["duration"]/365):
        print(f"{FAIL}PT3 fails: 'duration_year' not properly calculated.{ENDC}")
        return 0

    # confirm to tester that all looks good!
    print(f"{OKGREEN}PT3 passes!{ENDC}")
    return 1


if __name__ == "__main__":
    # run appropriate sections based on args
    if len(sys.argv) != 2:
        print(f"{FAIL}Error: Missing part of project to run.\
               \nUsage: python validate.py pt[1|2|3]{ENDC}")
    else:
        if sys.argv[1] == "pt1":
            pt1()
        elif sys.argv[1] == "pt2":
            pt1()
            pt2()
        elif sys.argv[1] == "pt3":
            pt1()
            pt2()
            pt3()
