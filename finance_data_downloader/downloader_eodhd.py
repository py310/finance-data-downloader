import os
import json
import requests
import pandas as pd
from downloader import Downloader

class Eodhd_Downloader(Downloader):

    def process_data(self, data_json:json) -> pd.DataFrame:

        return pd.json_normalize(data_json)

    def download_ticker_data(self, ticker):
        if self.uniq_name: ticker = self.uniq_name

        try:
            url = self.url.replace('!KEY', ticker).replace('!PRVT_KEY', self.private_key)
            response = requests.get(url, headers=self.headers, timeout=5)

            # Write the downloaded data to a file
            if response.status_code == 200:
                file_path = os.path.join(self.data_folder, f"{ticker}.{self.output_format}")
                response_json = response.json()

                if self.output_format == 'csv':
                    df = self.process_data(response_json)
                    df.to_csv(file_path, index=False)

                elif self.output_format == 'json':
                    with open(file_path, 'w') as f:
                        json.dump(response_json, f)

                return True
                
            else: return False
            
        except Exception:
            return False