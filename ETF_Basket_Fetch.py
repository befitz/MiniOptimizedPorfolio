#Get ETF Basket
import finnhub
import numpy as np
import pandas as pd
import requests
import config


#function to fetch basket holdings of an ETF. Takes in ETF ticker, returns
def Fetch_ETF_Basket(ETF):
    ETF = ETF
    finnhub_client = finnhub.Client(api_key=config.FINHUB_SANDBOX_API)
    data = (finnhub_client.etfs_holdings(f'{ETF}'))

    my_columns = ['Ticker', 'Security Name', 'Weight','No. of Shares held', 'Close Price', 'Weight*Close']
    final_dataframe = pd.DataFrame(columns = my_columns)

    for i in range(0, len(data['holdings'])):
        holdings = data['holdings'][i]
        final_dataframe = final_dataframe.append(
                    pd.Series(
                [         
                    holdings['symbol'],
                    holdings['name'],
                    holdings['percent']/100,
                    holdings['share'],
                    1,
                    1
                ],
                index = my_columns
                ),
                ignore_index=True
            )

    tickers = final_dataframe['Ticker']

    return tickers

def test_fetch(ETF):
    ETF = ETF
    #finnhub_client = finnhub.Client(api_key=config.FINHUB_API)
    data = requests.get(f'https://finnhub.io/api/v1/index/constituents?symbol=VO&token={config.FINHUB_API}')
    data2 = data.json()
    #data = finnhub_client.indices_const(symbol = f'{ETF}')
    print(data2)


test_fetch('VO')