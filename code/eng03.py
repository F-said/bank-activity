from code.BankingData import BankingData


class Transformer(BankingData):
    def transform(self):
        # now that we've ran self.load(), we can interact with "self.df"
        self.load()

        # TODO: rename "y" variable into "purchase_term"
        self.df = self.df.rename(columns=...)

        # TODO: engineer a new feature called "duration_year" which is the
        # "duration" column converted from days to years by dividing the
        # column by 365 ("duration_year" = "duration" / 365)
        # https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html#how-to-create-new-columns-derived-from-existing-columns
        self.df["duration_year"] = ...
