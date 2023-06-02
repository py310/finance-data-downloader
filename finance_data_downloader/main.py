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

# Define constants
CONFIG_FILE = 'config.ini'
LOG_FILE = 'data_downloader.log'

# Read the configuration file
def read_configuration():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config

# Set up logger
def setup_logger():
    logging.basicConfig(filename=LOG_FILE,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S',
                        level=logging.INFO)

# Create and configure the downloader object based on the section in the config
def create_downloader(config, section):
    downloader = None
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
                                       duration_of_work_min=int(config[section]['duration_of_work_min']))
    elif section == 'eurekahedge':
        downloader = Eurekahedge_Downloader(url=config[section]['url'],
                                            provider=config[section]['provider'],
                                            data_folder=config[section]['data_folder'],
                                            duration_of_work_min=int(config[section]['duration_of_work_min']),
                                            tickers_path=config[section]['tickers_path'])     
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

    It reads the configuration file, sets up the logger, creates downloader objects based on the configuration,
    and either runs the downloaders immediately or schedules them for future execution based on the configuration.
    """
    is_schedule = False

    setup_logger()
    config = read_configuration()

    data_providers = [
                      'fred',
                      'finyahoo_futures',
                      'finyahoo_equities',
                      'split_history',
                      'ishares',
                      'nasdaq',
                      'eurekahedge'
                      ]

    downloaders = {provider: create_downloader(config, provider) for provider in data_providers}

    if is_schedule:
        run_schedulers(config, downloaders)
    else:
        for downloader in downloaders.values():
            downloader.time_limited_download()


if __name__ == '__main__':
    main()