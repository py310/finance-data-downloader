import os
import requests
from downloader import Downloader

class iShares_Downloader(Downloader):

    def download_ticker_data(self, ticker):
        try:
            url = self.url.replace('!KEY', ticker)
            response = requests.get(url, headers=self.headers, timeout=5)

            # Write the downloaded data to a file
            if response.status_code == 200:
                # Extract the ticker name from the URL
                ticker_name = ticker.split('/')[-2]

                # Construct the file path using the ticker name
                file_path = os.path.join(self.data_folder, f"{ticker_name}.xls")

                # Write the downloaded data to the file
                with open(file_path, "wb") as f:
                    f.write(response.content)

                return True
            else:
                return False
            
        except Exception:
            return False