# Finance Data Downloader

Finance Data Downloader is a Python application that downloads data from various sources such as FRED (Federal Reserve Economic Data), FinYahoo (Yahoo Finance), SplitHistory, EODHD and more. It allows you to schedule and perform data downloads for different providers.

Supported providers include:

- FRED: Download economic data from [the Federal Reserve Economic Data](https://fred.stlouisfed.org/) repository.
- FinYahoo: Download financial data for futures and equities from [Yahoo Finance](https://finance.yahoo.com/).
- SplitHistory: Download [historical stock split data](https://www.splithistory.com/).
- Nasdaq: Download symbol change history from [Nasdaq](https://www.nasdaq.com/market-activity/stocks/symbol-change-history).
- iShares: Download data from [iShares](https://www.ishares.com/uk).
- Eurekahedge: Download data from [Eurekahedge](https://www.eurekahedge.com/Indices/).
- EODHD: Download various data from [EODHD](https://eodhd.com/).

You can either run the downloads on-demand or schedule them to run at specific times.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction
The Finance Data Downloader is a Python project that allows you to download financial data from different providers.

The project consists of the following files:
- `main.py`: The main script that sets up the logger, reads the configuration, creates the downloader objects, and launches the downloads either on schedule or manually.
- `downloader.py`: The base class for the downloader objects, containing common functionality for downloading data.
- `downloader_fred.py`: A derived class from `downloader.py`, specifically for downloading data from FRED.
- `downloader_finyahoo.py`: A derived class from `downloader.py`, specifically for downloading data from FinYahoo.
- `downloader_splithistory.py`: A derived class from `downloader.py`, specifically for downloading data from SplitHistory.
- `downloader_nasdaq.py`: A derived class from `downloader.py`, specifically for downloading data from Nasdaq.
- `downloader_ishares.py`: A derived class from `downloader.py`, specifically for downloading data from iShares.
- `downloader_eurekahedge.py`: A derived class from `downloader_ishares.py`, specifically for downloading data from Eurekahedge.
- `downloader_eodhd.py` and its subclasses: A derived class from `downloader.py`, specifically for downloading data from EODHD.
- `config.ini`: The configuration file containing the settings for each provider.
- `config_private.ini`: The configuration file containing private API keys.

## Installation
1. Clone the repository to your local machine: `git clone https://github.com/py310/finance-data-downloader.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the [configuration file](#configuration) `config.ini`:

## Usage
1. Open a terminal or command prompt and navigate to the project directory.
2. Set `is_schedule = True` in `main.py` if you want to run the downloads on schedule, or set it to `False` for manual execution.
3. Run the main script: `python main.py`
4. The script will start downloading the data based on the configuration settings and log the progress to the console and `data_downloader.log` file.

## Configuration
The `config.ini` file contains the configuration settings for each provider. You can modify these settings according to your requirements.

- `[provider_name]`: The section name for each provider.
- `url`: The URL for downloading data, where `!KEY` will be replaced with the actual ticker symbol.
- `tickers_path`: The file path to the CSV file containing the list of ticker symbols.
- `provider`: The name of the data provider.
- `data_folder`: The folder path where the downloaded data will be saved.
- `start_time`: The scheduled start time for downloading data (applicable when running on schedule).
- `duration_of_work_min`: The duration (in minutes) for which the downloader will work.
- `uniq_name`: The unique filename for single link downloads (optional).
- `output_format`: The output file format csv/json (optional).
- `docs_link`: The link to the documentation for the current API method (optional).

You can customize the configuration for other providers in a similar manner.

## License
This project is licensed under the [MIT License](LICENSE).
