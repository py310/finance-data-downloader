import json
import pandas as pd
from downloader_eodhd import Eodhd_Downloader

class Eodhd_IPOs_Downloader(Eodhd_Downloader):

    def process_data(self, data_json:json) -> pd.DataFrame:

        return pd.json_normalize(data_json['ipos'])