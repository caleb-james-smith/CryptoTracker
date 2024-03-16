# make_plots.py

# Make plots of crypto prices.
# Use the library cryptocompare. 
# https://pypi.org/project/cryptocompare/

import numpy as np
import cryptocompare
import datetime
import plot
import tools

# Get price over quarters
def getPriceOverQuarters(coin, currency, start_year, end_year):
    print(f" - Collecting price data over quarters: {coin} in {currency} over the year range [{start_year}, {end_year}]")
    prices = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13, 3):
            # for the end year, only include the first month
            if year == end_year and month > 1:
                break
            price_object = cryptocompare.get_historical_price(coin, currency, datetime.datetime(year,month,1))
            price = price_object[coin][currency]
            prices.append(price)
    return np.array(prices)

# Get price over years
def getPriceOverYears(coin, currency, start_year, end_year):
    print(f" - Collecting price data over years: {coin} in {currency} over the year range [{start_year}, {end_year}]")
    prices = []
    for year in range(start_year, end_year + 1):
        price_object = cryptocompare.get_historical_price(coin, currency, datetime.datetime(year,1,1))
        price = price_object[coin][currency]
        prices.append(price)
    return prices

# Make plots
def makePlots(plot_dir):
    start_year  = 2015
    end_year    = 2024
    coins       = ['BTC', 'ETH']
    
    for coin in coins:
        currency    = 'USD'
        
        # plot price vs years
        output_name = f"{plot_dir}/price_{coin}_in_{currency}_vs_years"
        title       = f"Price of {coin} in {currency}"
        x_label     = "Year"
        y_label     = f"Price ({currency})"
        
        # include the end year
        x_values    = np.arange(start_year, end_year + 1)
        y_values    = getPriceOverYears(coin, currency, start_year, end_year)
        plot.plot_scatter(output_name, x_values, y_values, title, x_label, y_label)
        
        # plot price vs quarters
        output_name = f"{plot_dir}/price_{coin}_in_{currency}_vs_quarters"
        title       = f"Price of {coin} in {currency}"
        x_label     = "Year (Quarters)"
        y_label     = f"Price ({currency})"
        
        # only inclue the first quarter of the end year
        x_values    = np.arange(start_year, end_year + 0.25, 0.25)
        y_values    = getPriceOverQuarters(coin, currency, start_year, end_year)
        plot.plot_scatter(output_name, x_values, y_values, title, x_label, y_label)

def main():
    print("It's go time.")
    
    #price_object = cryptocompare.get_price('BTC', currency='USD')
    #print(price_object['BTC']['USD'])
    #prices = getPriceOverYears('BTC', 'USD', 2015, 2020)
    #print(prices)

    plot_dir = "plots"
    tools.makeDir(plot_dir)
    makePlots(plot_dir)
    
    print("Done.")

if __name__ == "__main__":
    main()


