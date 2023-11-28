def calculate_annual_growth(total_growth, years):
    """ Beräknar genomsnittlig årlig tillväxt för en aktie. """
    end_value = 1 + (total_growth / 100)
    return (end_value ** (1/years)) - 1

def average_inflation(start_year, end_year, inflation_data):
    """ Beräknar genomsnittlig årlig inflation mellan två år. """
    inflation_rates = [inflation_data[year] for year in range(start_year, end_year + 1)]
    return sum(inflation_rates) / len(inflation_rates)

def average_stock_return(start_year, end_year, stock_return_data):
    """ Beräknar genomsnittlig årlig aktieavkastning mellan två år. """
    stock_returns = [stock_return_data[year] for year in range(start_year, end_year + 1)]
    return sum(stock_returns) / len(stock_returns)

def calculate_stock_performance(inflation_data, stock_return_data):
    stock_name = input("Ange aktiens namn: ")
    start_year = int(input("Ange startår för aktieinvesteringen (från och med 1984): "))
    end_year = int(input("Ange slutår för aktieinvesteringen: "))
    total_growth = float(input("Ange den totala värdestegringen i procent: "))

    if start_year < 1984 or end_year > 2023:
        return "Tyvärr, vi har bara data om aktieavkastningen från 1984 till 2023."

    stock_annual_growth = calculate_annual_growth(total_growth, end_year - start_year)
    avg_stock_return = average_stock_return(start_year, end_year, stock_return_data)
    avg_inflation = average_inflation(start_year, end_year, inflation_data)

    performance_comment = ("Aktien " + stock_name + " har haft en genomsnittlig årlig tillväxt på " +
                           f"{stock_annual_growth * 100:.2f}%, jämfört med börsens genomsnittliga årliga avkastning på " +
                           f"{avg_stock_return:.2f}% och den genomsnittliga årliga inflationen på " +
                           f"{avg_inflation:.2f}% under samma period.")
    return performance_comment

# Data för aktieavkastningen
stock_return_data = {
    1984: -16.90, 1985: 37.10, 1986: 45.30, 1987: -16.70, 1988: 51.80,
    1989: 30.60, 1990: -27.90, 1991: 11.00, 1992: 7.60, 1993: 53.10,
    1994: 3.40, 1995: 18.80, 1996: 37.20, 1997: 29.40, 1998: 16.90,
    1999: 71.00, 2000: -11.90, 2001: -19.80, 2002: -41.70, 2003: 29.00,
    2004: 16.60, 2005: 29.40, 2006: 19.50, 2007: -5.70, 2008: -38.80,
    2009: 43.70, 2010: 21.40, 2011: -14.50, 2012: 11.80, 2013: 20.70,
    2014: 9.90, 2015: -1.20, 2016: 4.90, 2017: 3.93, 2018: -5.13,
    2019: 25.78, 2020: 5.49, 2021: 28.90, 2022: -18.41, 2023: 8.90
}

# Inflationsdata för Sverige (genomsnittlig årlig inflation)
inflation_data = {
    1984: 8.0, 1985: 7.4, 1986: 4.2, 1987: 4.2, 1988: 5.8, 1989: 6.5, 1990: 10.5, 1991: 9.3,
    1992: 2.6, 1993: 4.7, 1994: 2.4, 1995: 2.5, 1996: 0.8, 1997: 0.8, 1998: -0.5, 1999: 0.4,
    2000: 1.0, 2001: 2.3, 2002: 2.1, 2003: 1.9, 2004: 0.3, 2005: 0.5, 2006: 1.5, 2007: 2.2,
    2008: 3.4, 2009: -0.3, 2010: 1.2, 2011: 3.0, 2012: 0.9, 2013: 0.0, 2014: -0.2, 2015: 0.0,
    2016: 1.0, 2017: 1.8, 2018: 2.0, 2019: 1.8, 2020: 0.3, 2021: 2.3, 2022: 7.9, 2023: 9.4
}

# Kör programmet
print(calculate_stock_performance(inflation_data, stock_return_data))

