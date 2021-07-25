# MiniOptimizedPorfolio

Takes in ETF stock symbol and returns the descrete allocation, remaining funds, portfolio perfomrance, and dataframe (of company name, ticker, and suggested allocation)

Input Example:
`MiniOptimizedPortfolio('IWR', 3000)`

Output Example:
`Discrete Allocation: {'MSCI': 1, 'IQV': 2, 'TROW': 2, 'TT': 2, 'IDXX': 1, 'INFO': 2, 'TWTR': 2}
Funds Remaining: $ 37.28997802734375
Expected annual return: 94.9%
Annual volatility: 17.8%
Sharpe Ratio: 5.22
(0.9488837254606892, 0.1780603494893059, 5.216679222099791)
                company_name  ... Discrete_val_3000
0                  MSCI Inc.  ...                 1
1        IQVIA Holdings Inc.  ...                 2
2  T. Rowe Price Group, Inc.  ...                 2
3     Trane Technologies plc  ...                 2
4   IDEXX Laboratories, Inc.  ...                 1
5            IHS Markit Ltd.  ...                 2
6              Twitter, Inc.  ...                 2`

## scrape_stock_symbols(ETF_Ticker)

Takes in ETF stock symbol, returns a list of holdings

Input Example:
`company_tickers = scrape_stock_symbols('IWR')
print(company_tickers)`

Output Exaple:

`['DOCU', 'IDXX', 'TWTR', 'CMG', 'ROKU', 'TT', 'MRVL', 'TROW', 'IQV', 'A', 'MSCI', 'VEEV', 'DXCM', 'MTCH', 'INFO']`


## Historical_Prices_Fetch(ETF_Ticker, Period)

Takes in ETF ticker and period, returns a formated dataframe with historical prices for each ticker in the basket

Input Example:
`df = Historical_Prices_Fetch('IWR', '6mo')
print(df.head())`

Output Example:
`Symbol               A          CMG  ...       TWTR        VEEV
Date                                 ...                       
2021-01-25  125.124901  1486.319946  ...  47.840000  292.500000
2021-01-26  123.569305  1489.250000  ...  49.669998  292.220001
2021-01-27  118.463799  1466.359985  ...  48.189999  279.970001
2021-01-28  121.215981  1480.540039  ...  51.570000  280.000000`

