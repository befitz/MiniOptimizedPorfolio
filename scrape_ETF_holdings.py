#Scrape ETF database for the top 15 holdings of a given ETF
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


def scrape_stock_symbols(Ticker):
	company_tickers = []
	Ticker = Ticker.upper()
	URL = f'https://etfdb.com/etf/{Ticker}/#holdings'
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	results = soup.find_all(attrs={"data-th": "Symbol"})
	result_counter = 0
	for result in results:
		try:
			i_result = results[result_counter]
			company_tickers.append(i_result.find('a').text)
		except:
			company_tickers.append('N/A')
		result_counter += 1
	
	return company_tickers


def scrape_company_name(Ticker):
	company_name = []
	Ticker = Ticker.upper()
	URL = f'https://etfdb.com/etf/{Ticker}/#holdings'
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	results = soup.find_all(attrs={"data-th": "Holding"})
	result_counter = 0
	for result in results:
		try:
			i_result = results[result_counter]
			company_name.append(i_result.text)
		except:
			pass
		result_counter += 1
	
	return company_name

