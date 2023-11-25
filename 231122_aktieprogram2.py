def calculate_annual_return(value_increase, years):
    """ Beräknar genomsnittlig årlig avkastning. """
    end_value = 1 + (value_increase / 100)  # Omvandlar procentuell ökning till multiplikativ faktor
    return (end_value ** (1/years)) - 1

def average_inflation(start_year, end_year, inflation_data):
    """ Beräknar genomsnittlig årlig inflation mellan två år. """
    inflation_rates = [inflation_data[year] for year in range(start_year, end_year + 1)]
    return sum(inflation_rates) / len(inflation_rates)

# Huvudfunktion för att beräkna och jämföra aktieförändringen med inflationen
def calculate_stock_performance(inflation_data):
    stock_name = input("Ange aktiens namn: ")
    value_increase = float(input("Ange värdestegringen i procent: "))
    start_year = int(input("Ange startår (från och med 1980): "))
    end_year = int(input("Ange slutår: "))

    if start_year < 1980 or end_year > 2023:
        return "Tyvärr, vi har bara data om inflationen från 1980 till 2023."

    annual_return = calculate_annual_return(value_increase, end_year - start_year)
    avg_inflation = average_inflation(start_year, end_year, inflation_data)

    performance_comment = ("Aktien " + stock_name + " har haft en genomsnittlig årlig föräntning på " +
                           f"{annual_return * 100:.2f}% per år, " +
                           "vilket är " + ("högre" if annual_return < avg_inflation else "lägre") +
                           " än den genomsnittliga årliga inflationen på " +
                           f"{avg_inflation:.2f}% under samma period.")
    return performance_comment

# Förenklad inflationsdata för Sverige (genomsnittlig årlig inflation)
inflation_data = {
    1980: 13.4, 1981: 11.8, 1982: 8.6, 1983: 8.9, 1984: 8.0, 1985: 7.4, 1986: 4.2, 1987: 4.2,
    1988: 5.8, 1989: 6.5, 1990: 10.5, 1991: 9.3, 1992: 2.6, 1993: 4.7, 1994: 2.4, 1995: 2.5,
    1996: 0.8, 1997: 0.8, 1998: -0.5, 1999: 0.4, 2000: 1.0, 2001: 2.3, 2002: 2.1, 2003: 1.9,
    2004: 0.3, 2005: 0.5, 2006: 1.5, 2007: 2.2, 2008: 3.4, 2009: -0.3, 2010: 1.2, 2011: 3.0,
    2012: 0.9, 2013: 0.0, 2014: -0.2, 2015: 0.0, 2016: 1.0, 2017: 1.8, 2018: 2.0, 2019: 1.8,
    2020: 0.3, 2021: 2.3, 2022: 7.9, 2023: 9.4  # Exempel på data för senare år
}

# Kör programmet
print(calculate_stock_performance(inflation_data))
