import os
import requests
from downloader import Downloader

class iShares_Downloader(Downloader):

    def download_ticker_data(self, ticker_url):
        try:
            response = requests.get(ticker_url, headers=self.headers, timeout=5)

            # Write the downloaded data to a file
            if response.status_code == 200:
                # Extract the ticker name from the URL
                file_name = response.headers.get('content-disposition').split('=')[1]

                # Construct the file path using the ticker name
                file_path = os.path.join(self.data_folder, f"{file_name}")

                # Write the downloaded data to the file
                with open(file_path, "wb") as f:
                    f.write(response.content)

                return True
            else:
                return False
            
        except Exception:
            return False