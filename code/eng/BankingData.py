import pandas as pd

import time
from datetime import datetime


class BankingData:
    def __init__(self, path):
        self.path = path
        self.df = None

    def load(self):
        # to keep us in compliance with EU standards,
        # we must log the datetime all data loads
        epoch = time.time()
        self._date = datetime.utcfromtimestamp(epoch).\
            strftime('%Y-%m-%d %H:%M:%S')

        self.df = pd.read_csv(self.path)

    def write(self, new_path):
        self.df.to_csv(new_path, index=False)
