import pandas as pd
from downloader_eodhd import Eodhd_Downloader

class Eodhd_Tickers_Downloader(Eodhd_Downloader):

    def read_tickers_from_file(self):
        tickers_df = pd.read_csv(self.tickers_path, sep=',')
        self.tickers = tickers_df['Code'].tolist()
        return self