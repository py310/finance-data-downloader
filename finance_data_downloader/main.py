import time
import logging
import schedule
import threading
import configparser
from downloader_fred import Fred_Downloader
from downloader_finyahoo import FinYahoo_Downloader
from downloader_splithistory import SplitHistory_Downloader
from downloader_ishares import iShares_Downloader
from downloader_nasdaq import Nasdaq_Downloader
from downloader_eurekahedge import Eurekahedge_Downloader
from downloader_eodhd import Eodhd_Downloader
from downloader_eodhd_capitalizations import Eodhd_Capitalizations_Downloader
from downloader_eodhd_sentiment import Eodhd_Sentiment_Downloader
from downloader_eodhd_macro import Eodhd_Macro_Downloader
from downloader_eodhd_tickers import Eodhd_Tickers_Downloader
from downloader_eodhd_earnings import Eodhd_Earnings_Downloader
from downloader_eodhd_ipos import Eodhd_IPOs_Downloader

# Define constants
CONFIG_FILE = 'config.ini'
CONFIG_FILE_PRVT = 'config_private.ini'
LOG_FILE = 'data_downloader.log'

# Read the configuration file
def read_configuration(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

# Set up logger
def setup_logger():
    logging.basicConfig(filename=LOG_FILE,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S',
                        level=logging.INFO)

# Create and configure the downloader object based on the section in the config
def create_downloader(config, config_prvt, section):
    downloader = None
    section_prvt = section.split('_')[0]

    if section == 'fred':
        downloader = Fred_Downloader(url=config[section]['url'],
                                     provider=config[section]['provider'],
                                     data_folder=config[section]['data_folder'],
                                     duration_of_work_min=int(config[section]['duration_of_work_min']),
                                     tickers_path=config[section]['tickers_path'])
    elif section.startswith('finyahoo'):
        downloader = FinYahoo_Downloader(url=config[section]['url'],
                                         provider=config[section]['provider'],
                                         data_folder=config[section]['data_folder'],
                                         duration_of_work_min=int(config[section]['duration_of_work_min']),
                                         tickers_path=config[section]['tickers_path'])
    elif section == 'split_history':
        downloader = SplitHistory_Downloader(url=config[section]['url'],
                                             provider=config[section]['provider'],
                                             data_folder=config[section]['data_folder'],
                                             duration_of_work_min=int(config[section]['duration_of_work_min']),
                                             tickers_path=config[section]['tickers_path'])
    elif section == 'ishares':
        downloader = iShares_Downloader(url=config[section]['url'],
                                        provider=config[section]['provider'],
                                        data_folder=config[section]['data_folder'],
                                        duration_of_work_min=int(config[section]['duration_of_work_min']),
                                        tickers_path=config[section]['tickers_path'])
    elif section == 'nasdaq':
        downloader = Nasdaq_Downloader(url=config[section]['url'],
                                       provider=config[section]['provider'],
                                       data_folder=config[section]['data_folder'],
                                       duration_of_work_min=int(config[section]['duration_of_work_min']),
                                       uniq_name = config[section]['uniq_name'])
    elif section == 'eurekahedge':
        downloader = Eurekahedge_Downloader(url=config[section]['url'],
                                            provider=config[section]['provider'],
                                            data_folder=config[section]['data_folder'],
                                            duration_of_work_min=int(config[section]['duration_of_work_min']),
                                            tickers_path=config[section]['tickers_path'])
    elif section == 'eodhd_capitalizations':
        downloader = Eodhd_Capitalizations_Downloader(url=config[section]['url'],
                                                      provider=config[section]['provider'],
                                                      data_folder=config[section]['data_folder'],
                                                      duration_of_work_min=int(config[section]['duration_of_work_min']),
                                                      tickers_path=config[section]['tickers_path'],
                                                      output_format = config[section]['output_format'],
                                                      private_key = config_prvt[section_prvt]['private_key'])
    elif section.endswith('sentiment'):
        downloader = Eodhd_Sentiment_Downloader(url=config[section]['url'],
                                                provider=config[section]['provider'],
                                                data_folder=config[section]['data_folder'],
                                                duration_of_work_min=int(config[section]['duration_of_work_min']),
                                                tickers_path=config[section]['tickers_path'],
                                                output_format = config[section]['output_format'],
                                                private_key = config_prvt[section_prvt]['private_key'])        
    elif section == 'eodhd_macro_indicators_us':
        downloader = Eodhd_Macro_Downloader(url=config[section]['url'],
                                            provider=config[section]['provider'],
                                            data_folder=config[section]['data_folder'],
                                            duration_of_work_min=int(config[section]['duration_of_work_min']),
                                            tickers_path=config[section]['tickers_path'],
                                            output_format = config[section]['output_format'],
                                            private_key = config_prvt[section_prvt]['private_key'])
    elif section in ['eodhd_tickers', 'eodhd_exchange_details']:
        downloader = Eodhd_Tickers_Downloader(url=config[section]['url'],
                                              provider=config[section]['provider'],
                                              data_folder=config[section]['data_folder'],
                                              duration_of_work_min=int(config[section]['duration_of_work_min']),
                                              tickers_path=config[section]['tickers_path'],
                                              output_format = config[section]['output_format'],
                                              private_key = config_prvt[section_prvt]['private_key'])    
    elif section == 'eodhd_ipos':
        downloader = Eodhd_IPOs_Downloader(url=config[section]['url'],
                                           provider=config[section]['provider'],
                                           data_folder=config[section]['data_folder'],
                                           duration_of_work_min=int(config[section]['duration_of_work_min']),
                                           output_format = config[section]['output_format'],
                                           uniq_name = config[section]['uniq_name'], 
                                           private_key = config_prvt[section_prvt]['private_key'])
    elif section == 'eodhd_earnings':
        downloader = Eodhd_Earnings_Downloader(url=config[section]['url'],
                                               provider=config[section]['provider'],
                                               data_folder=config[section]['data_folder'],
                                               duration_of_work_min=int(config[section]['duration_of_work_min']),
                                               tickers_path=config[section]['tickers_path'],
                                               output_format = config[section]['output_format'],
                                               private_key = config_prvt[section_prvt]['private_key'])
    elif section in ['eodhd_renamings', 'eodhd_exchanges', 'eodhd_events']:
        downloader = Eodhd_Downloader(url=config[section]['url'],
                                      provider=config[section]['provider'],
                                      data_folder=config[section]['data_folder'],
                                      duration_of_work_min=int(config[section]['duration_of_work_min']),
                                      output_format = config[section]['output_format'],
                                      uniq_name = config[section]['uniq_name'], 
                                      private_key = config_prvt[section_prvt]['private_key'])           
    elif section.startswith('eodhd'):
        downloader = Eodhd_Downloader(url=config[section]['url'],
                                      provider=config[section]['provider'],
                                      data_folder=config[section]['data_folder'],
                                      duration_of_work_min=int(config[section]['duration_of_work_min']),
                                      tickers_path=config[section]['tickers_path'],
                                      output_format = config[section]['output_format'],
                                      private_key = config_prvt[section_prvt]['private_key'])
    return downloader

# Create threads for parallel execution
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

# Launch scheduled downloads
def run_schedulers(config, downloaders):
    for section, downloader in downloaders.items():
        schedule_time = config[section]['start_time']
        schedule.every().day.at(schedule_time).do(run_threaded, downloader.time_limited_download)
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    """
    The main function that orchestrates the data download process.

    It reads the configuration files, sets up the logger, creates downloader objects based on the configuration,
    and either runs the downloaders immediately or schedules them for future execution based on the configuration.
    """
    is_schedule = False

    setup_logger()
    config = read_configuration(CONFIG_FILE)
    config_prvt = read_configuration(CONFIG_FILE_PRVT)

    data_providers = [
                      'fred',
                      'finyahoo_futures',
                      'finyahoo_equities',
                      'split_history',
                      'ishares',
                      'nasdaq',
                      'eurekahedge',
                      'eodhd_capitalizations',
                      'eodhd_fundamentals',
                      'eodhd_news_sentiment',
                      'eodhd_twitter_sentiment',
                      'eodhd_renamings',
                      'eodhd_exchanges',
                      'eodhd_tickers',
                      'eodhd_macro_indicators_us',
                      'eodhd_news',
                      'eodhd_dividends',
                      'eodhd_splits',
                      'eodhd_exchange_details',
                      'eodhd_insiders',
                      'eodhd_earnings',
                      'eodhd_ipos',
                      'eodhd_events',
                      'eodhd_ohlc'
                      ]

    downloaders = {provider: create_downloader(config, config_prvt, provider) for provider in data_providers}

    if is_schedule:
        run_schedulers(config, downloaders)
    else:
        for downloader in downloaders.values():
            downloader.time_limited_download()


if __name__ == '__main__':
    main()