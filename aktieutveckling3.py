def calculate_annual_return(value_increase, years):
    """ Beräknar genomsnittlig årlig avkastning. """
    end_value = 1 + (value_increase / 100)  # Omvandlar procentuell ökning till multiplikativ faktor
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

    if start_year < 1984 or end_year > 2023:
        return "Tyvärr, vi har bara data om aktieavkastningen från 1984 till 2023."

    avg_stock_return = average_stock_return(start_year, end_year, stock_return_data)
    avg_inflation = average_inflation(start_year, end_year, inflation_data)

    performance_comment = ("Aktien " + stock_name + " har haft en genomsnittlig årlig avkastning på " +
                           f"{avg_stock_return:.2f}% per år, " +
                           "jämfört med den genomsnittliga årliga inflationen på " +
                           f"{avg_inflation:.2f}% under samma period.")
    return performance_comment

# Data för aktieavkastningen
stock_return_data = {
    # Här ska du lägga in data för varje år från 1984 till 2023
}

# Inflationsdata (som tidigare)
inflation_data = {
    # Dina tidigare inflationsdata
}

# Kör programmet
print(calculate_stock_performance(inflation_data, stock_return_data))

