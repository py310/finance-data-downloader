import os
import time
import pandas as pd
from downloader import Downloader

class SplitHistory_Downloader(Downloader):

    def process_splits_data(self, df:pd.DataFrame) -> pd.DataFrame:
        df = pd.DataFrame(df.values[1:], columns=df.iloc[0])
        df['Date'] = pd.to_datetime(df['Date'])
        df.rename(columns={'Ratio':'Ratio_text'}, inplace=True)
        if not df.empty:
            df[['Value1', 'Value2']] = df['Ratio_text'].str.split(" for ", expand=True).astype(int)
            df['Ratio'] = round(df['Value1'] / df['Value2'], 4)
        return df
   
    def download_ticker_data(self, ticker):
        try:
            url = self.url.replace('!KEY', ticker)
            dfs = pd.read_html(url)
            # Find correct table (DataFrame)
            for df in dfs:
                if 'Ratio' in df.iloc[0].tolist():
                    processed_df = self.process_splits_data(df)
                    # Write the downloaded data to a file
                    file_path = os.path.join(self.data_folder, f"{ticker}.csv")
                    processed_df.to_csv(file_path, index=False)
                    return True
            return False
        except:
            return False