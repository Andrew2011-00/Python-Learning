currencies = {}

currencies["RUB"] = 2.98
currencies["ARS"] = 0.82
currencies["HNL"] = 0.17
currencies["AUD"] = 1.9622
currencies["MAD"] = 0.208

while True:
    try:
        conicoins = float(input())
    except ValueError:
        print("Please use numbers only")
    else:
        for currency in currencies:
            print(f"I will get {round(currencies[currency] * conicoins, 2)} {currency} from the sale of {conicoins} conicoins")
        break