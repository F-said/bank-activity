from BankingData import BankingData


class Cleaner(BankingData):
    def clean(self, path):
        # now that we've ran self.load(), we can interact with "self.df"
        self.load()

        # drop all rows with null values
        self.df = ...

        # convert str to int
        self.df = ...

        # remove extreme financial outliers
        # (these customers should be contacted by our private clientele dept.)
        self.df = ...

        # after completing our cleaning steps, let's write this data out
        self.write(path)
