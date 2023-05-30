import os
import time
import logging
import requests
import pandas as pd

class Nasdaq_Downloader():
    def __init__(self, url:str, provider:str, data_folder:str, duration_of_work_min:int):
        self.url = url
        self.provider = provider
        self.data_folder = data_folder
        self.duration_of_work_sec = duration_of_work_min * 60
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

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

    def data_download(self):
        # Create data folder if it doesn't exist
        os.makedirs(self.data_folder, exist_ok=True)
        try:
            response = requests.get(self.url, headers=self.headers, timeout=5)
            if response.status_code == 200:
                
                # Format response data
                response_json = response.json()
                df = self.process_data(response_json)

                # Write the downloaded data to the file
                file_path = os.path.join(self.data_folder, f"renaming.csv")
                df.to_csv(file_path)

                return True
            else:
                return False
            
        except Exception:
            return False

    def time_limited_download(self):
        logging.info(f"{self.provider} - Data downloader started.")

        # Get the start time of the downloader
        start_time = time.time()

        # Continue downloading until there are no remaining tickers or the duration of work is reached
        success = False
        while not success and time.time() - start_time < self.duration_of_work_sec:
            success = self.data_download()
            time.sleep(5)

        if not success:
            # Log unsuccessful completion
            logging.warning(f"{self.provider} - Download unsuccessfully.")
        else:
            # Log successful completion
            logging.info(f"{self.provider} - Download successfully.")
        return self