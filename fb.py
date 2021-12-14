import yfinance as yf
import pandas as pd
from compute_black_scholes import *
import matplotlib.pyplot as plt

fb = yf.Ticker("FB")
risk = .01426

time_to_expiry = 31/365
current_price = 330.34

# chain1 = fb.options
# print(chain1)

jan_14th_exp = fb.option_chain('2022-01-14')

# # combine all dataframes into a single dataframe
df = pd.concat(jan_14th_exp)

df.to_csv('fb.csv')

implied_vol = df['impliedVolatility']

strike = df['strike']
options_prices = df['lastPrice']

bid = df['bid']
ask = df['ask']

avg = []
for i in range(40):
    temp = bid[i] + ask[i]
    avg = bid/2


vol_arr = implied_vol.values
strike_arr = strike.values 
price_arr = avg.values




arr_size = strike_arr.size
empirical_prices = np.zeros(arr_size)

for x in range(arr_size):
    empirical_prices[x] = BS_CALL(current_price, strike_arr[x], time_to_expiry, risk, vol_arr[x])
# print(empirical_prices)

difference = price_arr - empirical_prices

# assigning x and y coordinates

strikes = strike_arr[:40]
emp_prices = empirical_prices[:40]
act_prices = price_arr[:40]
# plot_diffs = difference



 
# depicting the visualization
plot1 = plt.figure(1)
plt.plot(strikes, emp_prices, color='red')
plt.plot(strikes, act_prices, color='green')

plt.xlabel('Strike Price')
plt.ylabel('Option price')
 
# displaying the title
plt.title("Strike prices vs Options price")

plot2 = plt.figure(2)
plt.plot(strikes, difference[:40], color = 'red')

plt.xlabel('Strike Price')
plt.ylabel('Difference in Predicted Option Price and Actual Option Price')
 
# displaying the title
plt.title("Predicted Option Price vs Actual")






 
plt.show()
