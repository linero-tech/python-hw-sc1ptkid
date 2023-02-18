from to_do import TODO


def task1():
    country = "panama"
    capital = "panama city"
    currency = "usd"
    country_name = f"Country:{country.title()}\nCapital:{capital.title()}\nCurrency:{currency.upper()}"
    return country_name


if __name__ == "__main__":
    print(task1())
