# MiniOptimizedPorfolio

Takes in ETF stock symbol and returns the descrete allocation, remaining funds, portfolio perfomrance, and dataframe (of company name, ticker, and suggested allocation)

Example:

```MiniOptimizedPortfolio('IWR', 3000)```

## scrape_stock_symbols(ticker)

Takes in ETF stock symbol, returns a list of holdings


Example:

```company_tickers = scrape_stock_symbols('IWR')```


## Historical_Prices_Fetch()

Takes in ETF ticker and period, returns a formated dataframe with historical prices for each ticker in the basket

Example:

```df = Historical_Prices_Fetch('IWR', '6mo')```


