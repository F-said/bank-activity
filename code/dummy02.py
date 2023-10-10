from code.BankingData import BankingData
import pandas as pd


class Dummify(BankingData):
    def encode(self):
        # now that we've ran self.load(), we can interact with "self.df"
        self.load()

        # TODO: convert the "jobs" & "education" columns into "dummy variables"
        # https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html
        # further explanation here: https://www.geeksforgeeks.org/how-to-create-dummy-variables-in-python-with-pandas/
        dummy_vars = pd.get_dummies(self.df, columns=..., drop_first=True)

        self.df = dummy_vars
