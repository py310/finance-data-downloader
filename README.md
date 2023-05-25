# Finance Data Downloader

Finance Data Downloader is a Python application that downloads data from various sources such as FRED (Federal Reserve Economic Data), FinYahoo (Yahoo Finance), and SplitHistory. It allows you to schedule and perform data downloads for different providers.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction
The Finance Data Downloader is a Python project that utilizes the `schedule` library to schedule and perform data downloads. It supports multiple providers, including FRED, FinYahoo (for futures and equities), and SplitHistory. You can either run the downloads on-demand or schedule them to run at specific times.

The project consists of the following files:
- `main.py`: The main script that sets up the logger, reads the configuration, creates the downloader objects, and launches the downloads either on schedule or manually.
- `downloader.py`: The base class for the downloader objects, containing common functionality for downloading data.
- `downloader_finyahoo.py`: A derived class from `downloader.py`, specifically for downloading data from FinYahoo.
- `downloader_fred.py`: A derived class from `downloader.py`, specifically for downloading data from FRED.
- `downloader_splithistory.py`: A derived class from `downloader.py`, specifically for downloading data from SplitHistory.
- `config.ini`: The configuration file containing the settings for each provider.

## Installation
1. Clone the repository to your local machine: `git clone https://github.com/py310/finance-data-downloader.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the [configuration file](#configuration):

## Usage
1. Open a terminal or command prompt and navigate to the project directory.
2. Run the main script: `python main.py`
   - If you want to run the downloads on schedule, set `is_schedule = True` in `main.py`.
   - If you want to run the downloads manually, set `is_schedule = False` in `main.py`.
3. The script will start downloading the data based on the configuration settings and log the progress to the console and `data_downloader.log` file.

## Configuration
The `config.ini` file contains the configuration settings for each provider. You can modify these settings according to your requirements.

- `url`: The URL for downloading data, where `!KEY` will be replaced with the actual ticker symbol.
- `tickers_path`: The file path to the CSV file containing the list of ticker symbols.
- `provider`: The name of the data provider.
- `data_folder`: The folder path where the downloaded data will be saved.
- `start_time`: The scheduled start time for downloading data (applicable when running on schedule).
- `duration_of_work_min`: The duration (in minutes) for which the downloader will work.

You can customize the configuration for other providers in a similar manner.

## License
This project is licensed under the [MIT License](LICENSE).
