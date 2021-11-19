from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt import objective_functions
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from Historical_Prices_Fetch import *



def Calculate_Cleaned_Weights(df, ETF_Ticker):
	"""
	Function to calculate the annulized returns and annualized sample covariance matrix of the daily asset returns
	PYPorfolioOpt user guide - https://pyportfolioopt.readthedocs.io/en/latest/UserGuide.html
	args: df (pd.DataFrame), ETF_Ticker (string) if crypto, should be "crypto"
	"""
	mu = expected_returns.mean_historical_return(df)
	S = CovarianceShrinkage(df).ledoit_wolf()
	ef = EfficientFrontier(mu, S)#Create the efficient frontier object
	#ef.add_objective(objective_functions.L2_reg, gamma=0.1)
	weights = ef.max_sharpe()#Optimize for the maximal Sharpe ratio (how much excess return given the risk)
	if ETF_Ticker = "crypto":
		cleaned_weights = ef
	else:
		cleaned_weights = ef.clean_weights()

	return cleaned_weights, ef


def Calculate_Descrete_Allocation(clean_weights, portfolio_val, df):
	"""
	Function to calculate the descrete allocation using the weights previously cleaned (to a whole value if not crypto)
	args: clean_weights (list) portfolio_val (int), df (pd.DataFrame)
	returns: allocation (list), leftover (float), and descrete_allocation_list (list)
	"""
	descrete_allocation_list = []
	latest_prices = get_latest_prices(df)
	da = DiscreteAllocation(clean_weights, latest_prices, total_portfolio_value = portfolio_val)
	allocation, leftover = da.greedy_portfolio() #store the stock allocations and leftover

	for symbol in allocation:
		descrete_allocation_list.append(allocation.get(symbol))


	return allocation, leftover, descrete_allocation_list




#Master function to take in ETF Ticker, portfolio value (integer) and return the suggested porfolio dataframe
def MiniOptimizedPortfolio(manual, ETF_Ticker, portfolio_val, manual_ticker_list):
	df = Historical_Prices_Fetch(manual, f'{ETF_Ticker}', '6mo', manual_ticker_list)
	company_name = scrape_company_name(f'{ETF_Ticker}')
	clean_weights, ef = Calculate_Cleaned_Weights(df, ETF_Ticker)
	allocation, leftover, descrete_allocation_list = Calculate_Descrete_Allocation(clean_weights, portfolio_val, df)

	print('Discrete Allocation:', allocation)
	print('Funds Remaining: $', leftover)

	portfolio_df = pd.DataFrame(columns = ['company_name', 'company_ticker', 'Descrete_val_'+str(portfolio_val)])
	#portfolio_df['company_name'] = company_name
	portfolio_df['company_ticker'] = allocation
	portfolio_df['Descrete_val_'+str(portfolio_val)] = descrete_allocation_list

	print(ef.portfolio_performance(verbose=True))
	print(portfolio_df)

manual_ticker_list = ["BTC-USD", "ETH-USD", "ADA-USD", "SOL-USD", "FIL-USD", "UNI-USD", "ONE-USD", "ADOM-USD"]
MiniOptimizedPortfolio('manual', "crypto", 5000, manual_ticker_list)
