import json
import pandas as pd
from downloader_eodhd import Eodhd_Downloader

class Eodhd_Capitalizations_Downloader(Eodhd_Downloader):

    def process_data(self, data_json:json) -> pd.DataFrame:

        data = []
        for value in data_json.values():
            data.append(value)

        return pd.DataFrame(data)