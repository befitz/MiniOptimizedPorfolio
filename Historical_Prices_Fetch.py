#Use list of tickers and fetch each ticker's historical stock prices to generate a dataframe
import pandas as pd
import yfinance as yf
import datetime
from scrape_ETF_holdings import *


#Function that takes in the ETF fund ticker and # of days to retrive -> returns the holdings historical prices
#manual is auto or manual, auto looks to scrape the holdings, manual requires you provide the list of securities
def Fetch_raw_dataframe(manual, ETF_Ticker, period, company_tickers):
	if manual == "auto":
		company_tickers = scrape_stock_symbols(f'{ETF_Ticker}') #returns a list of basket tickers
	else:
		company_tickers = company_tickers
	i=0
	dfs = []
	for i in range(0,len(company_tickers)):
		ticker = yf.Ticker(f"{company_tickers[i]}")
		try:
			df = ticker.history(period = period)
			df.insert(0,'Symbol', company_tickers[i])
			df = df.drop(['Dividends', 'Stock Splits', 'High', 'Low', 'Open', 'Volume'], axis=1)
			dfs.append(df)
			print(i, company_tickers[i], 'has been stored to results')
		except:
			print("No information for ticker # and symbol:")
			print(i, company_tickers[i])
			i+=1
			continue
		i=i+1
	results = pd.concat(dfs)

	return results


#takes in the raw dataframe and pivots it to prepare for optimization
def pivot_historical_prices(df):
	results = df.dropna(how = 'all')
	results = results.reset_index()
	final = pd.pivot_table(results, values = 'Close', index='Date', columns = 'Symbol')

	return final


#The function daddy
#Returns the formated final dataframe for MiniOptimizedPortfolio
def Historical_Prices_Fetch(manual, ETF_Ticker, period, company_tickers):
	ETF_Ticker = ETF_Ticker
	period = period
	raw_df =Fetch_raw_dataframe(manual, ETF_Ticker, period, company_tickers)
	final = pivot_historical_prices(raw_df)

	return final
