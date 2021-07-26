from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt import objective_functions
#Get the discrete allocation of each share per stock
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from Historical_Prices_Fetch import *



def Calculate_Cleaned_Weights(df):
	df = df
	#Calculate the expected annualized returns and the annualized sample covariance matrix of the daily asset returns
	#PYPorfolioOpt user guide - https://pyportfolioopt.readthedocs.io/en/latest/UserGuide.html
	mu = expected_returns.mean_historical_return(df)
	S = CovarianceShrinkage(df).ledoit_wolf()
	#Optimize for the maximal Sharpe ratio (how much excess return given the risk)
	ef = EfficientFrontier(mu, S)#Create the efficient frontier object
	#ef.add_objective(objective_functions.L2_reg, gamma=0.1)
	weights = ef.max_sharpe()
	cleaned_weights = ef.clean_weights()

	return cleaned_weights, ef


def Calculate_Descrete_Allocation(clean_weights, portfolio_val, df):
	descrete_allocation_list = []
	company_name = []
	weights = clean_weights
	portfolio_val = portfolio_val
	df = df
	latest_prices = get_latest_prices(df)
	da = DiscreteAllocation(weights, latest_prices, total_portfolio_value = portfolio_val)
	allocation, leftover = da.greedy_portfolio() #store the stock allocations and leftover

	for symbol in allocation:
		descrete_allocation_list.append(allocation.get(symbol))
	for symbol in allocation:
		company_info = yf.Ticker(f"{symbol}")
		company_name.append(company_info.info['longName'])

	return allocation, leftover, descrete_allocation_list, company_name

	


#Master function to take in ETF Ticker, portfolio value (integer) and return the suggested porfolio dataframe
def MiniOptimizedPortfolio(ETF_Ticker, portfolio_val):
	df = Historical_Prices_Fetch(f'{ETF_Ticker}', '6mo')
	clean_weights, ef = Calculate_Cleaned_Weights(df)
	allocation, leftover, descrete_allocation_list, company_name = Calculate_Descrete_Allocation(clean_weights, portfolio_val, df)

	print('Discrete Allocation:', allocation)
	print('Funds Remaining: $', leftover)

	portfolio_df = pd.DataFrame(columns = ['company_name', 'company_ticker', 'Descrete_val_'+str(portfolio_val)])
	portfolio_df['company_name'] = company_name
	portfolio_df['company_ticker'] = allocation
	portfolio_df['Descrete_val_'+str(portfolio_val)] = descrete_allocation_list

	print(ef.portfolio_performance(verbose=True))
	print(portfolio_df)


MiniOptimizedPortfolio('BBMC', 3000)
