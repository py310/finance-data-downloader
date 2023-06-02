import os
import time
import logging
import requests
import pandas as pd
from downloader import Downloader

class Nasdaq_Downloader(Downloader):

    def process_data(self, data:dict) -> pd.DataFrame:
        # Extract the relevant data from the JSON
        data_list = data["data"]["symbolChangeHistoryTable"]["rows"]

        # Create and format a DataFrame from the extracted data
        df = pd.DataFrame.from_dict(data_list)
        df = df[["effective", "oldSymbol", "newSymbol", "companyName"]]
        df["effective"] = pd.to_datetime(df["effective"])
        df.rename(columns={"effective":"date"}, inplace=True)
        df.set_index("date", drop=True, inplace=True)
        return df

    def download_ticker_data(self, ticker):
        ticker = "renaming"
        try:
            response = requests.get(self.url, headers=self.headers, timeout=5)

            if response.status_code == 200:
                # Format response data
                response_json = response.json()
                df = self.process_data(response_json)

                # Write the downloaded data to the file
                file_path = os.path.join(self.data_folder, f"{ticker}.csv")
                df.to_csv(file_path)

                return True
                
            else: return False
            
        except Exception:
            return False