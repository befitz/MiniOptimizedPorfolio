#Scrape ETF database for the top 15 holdings of a given ETF
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

company_ticker = []

def scrape_stock_symbols(Ticker):
	Ticker = Ticker.upper()
	URL = f'https://etfdb.com/etf/{Ticker}/#holdings'
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	results = soup.find_all(attrs={"data-th": "Symbol"})
	result_counter = 0
	for result in results:
		i_result = results[result_counter]
		company_ticker.append(i_result.find('a').text)
		result_counter += 1
	
	print(company_ticker)



scrape_stock_symbols('IWR')