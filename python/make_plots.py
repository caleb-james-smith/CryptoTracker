# make_plots.py

import cryptocompare
import datetime
import plot
import tools

def getPriceOverYears(coin, currency, start_year, end_year):
    prices = []
    for year in range(start_year, end_year + 1):
        price_object = cryptocompare.get_historical_price(coin, currency, datetime.datetime(year,1,1))
        price = price_object[coin][currency]
        prices.append(price)
    return prices

def makePlots(plot_dir):
    start_year  = 2015
    end_year    = 2024
    coin        = 'BTC'
    currency    = 'USD'
    title       = f"Price of {coin} in {currency}"
    x_label     = "Year"
    y_label     = f"Price ({currency})"
    
    years = list(range(start_year, end_year + 1))
    prices = getPriceOverYears(coin, currency, start_year, end_year)
    plot.plot_scatter(years, prices, title, x_label, y_label)

def main():
    print("It's go time.")
    
    #price_object = cryptocompare.get_price('BTC', currency='USD')
    #print(price_object['BTC']['USD'])
    #prices = getPriceOverYears('BTC', 'USD', 2015, 2020)
    #print(prices)

    plot_dir = "plots"
    tools.makeDir(plot_dir)
    makePlots(plot_dir)

if __name__ == "__main__":
    main()

