import yfinance as yf
import pandas as pd

aapl = yf.Ticker("AAPL")
r_f = .01426

time_to_expiry = 32/365
current_price = 175.74

# chain1 = aapl.options

jan_14th_exp = aapl.option_chain('2022-01-14')

# combine all dataframes into a single dataframe
df = pd.concat(jan_14th_exp)

# save to csv
# df.to_csv('ticker.csv')

implied_vol = df['impliedVolatility']
strike = df['strike']

options_prices = df['lastPrice']


print(implied_vol)



