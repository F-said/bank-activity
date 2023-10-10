from code.BankingData import BankingData


class Cleaner(BankingData):
    def clean(self):
        # now that we've ran self.load(), we can interact with "self.df" as a
        # pandas dataframe
        self.load()

        # drop all rows with null values
        self.df = self.df.dropna()

        # remove quotes from balance column
        self.df.balance = self.df.balance.map(lambda x: x.strip("'"))

        # TODO: convert "balance" column from string to float
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html
        self.df["balance"] = ...

        # TODO: we aren't analyzing the "day" and "month" columns,
        #  so drop those specific columns
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html
        self.df = self.df.drop(columns=...)

        # TODO: we have a few financial outliers with extremely large balances
        # let's only keep balances less than €60,000
        # https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing
        self.df = self.df[...]
