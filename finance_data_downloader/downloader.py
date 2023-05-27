import os
import time
import logging
import requests
import pandas as pd

class Downloader:
    def __init__(self, url:str, tickers_path:str, provider:str, data_folder:str, duration_of_work_min:int):
        self.url = url
        self.tickers_path = tickers_path
        self.provider = provider
        self.data_folder = data_folder
        self.duration_of_work_sec = duration_of_work_min * 60
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        self.read_tickers_from_file()

    def read_tickers_from_file(self):
        tickers_df = pd.read_csv(self.tickers_path, names=['tickers'])
        self.tickers = tickers_df['tickers'].tolist()
        return self

    def data_download(self):
        # Create data folder if it doesn't exist
        os.makedirs(self.data_folder, exist_ok=True)

        # Iterate through the tickers and download data
        for ticker in self.tickers[:]:
            success = self.download_ticker_data(ticker)
            if success:
                self.tickers.remove(ticker)
            time.sleep(0.5)

        return self

    def download_ticker_data(self, ticker):

        url = self.url.replace('!KEY', ticker)
        response = requests.get(url, headers=self.headers, timeout=5)

        # Write the downloaded data to a file
        if response.status_code == 200:
            file_path = os.path.join(self.data_folder, f"{ticker}.csv")
            with open(file_path, "w") as f:
                f.write(response.text)
            return True
            
        else: return False

    def time_limited_download(self):
        logging.info(f"{self.provider} - Data downloader started.")

        # Get the start time of the downloader
        start_time = time.time()

        # Continue downloading until there are no remaining tickers or the duration of work is reached
        while self.tickers and time.time() - start_time < self.duration_of_work_sec:
            self.data_download()
            time.sleep(5)

        if self.tickers:
            # Log the tickers that couldn't be downloaded
            logging.warning(f"{self.provider} - Problematic tickers: {self.tickers}.")
        else:
            # Log successful completion if there are no remaining tickers
            logging.info(f"{self.provider} - Download completed successfully.")
        return self