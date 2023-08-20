data = {'date': '19.08.2023', 'bank': 'PB', 'baseCurrency': 980, 'baseCurrencyLit': 'UAH', 'exchangeRate': [{'baseCurrency': 'UAH', 'currency': 'AUD', 'saleRateNB': 
23.5319, 'purchaseRateNB': 23.5319}, {'baseCurrency': 'UAH', 'currency': 'AZN', 'saleRateNB': 21.5388, 'purchaseRateNB': 21.5388}, {'baseCurrency': 'UAH', 'currency': 'BYN', 'saleRateNB': 13.2919, 'purchaseRateNB': 13.2919}, {'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 27.0798, 'purchaseRateNB': 27.0798}, {'baseCurrency': 'UAH', 'currency': 'CHF', 'saleRateNB': 41.6831, 'purchaseRateNB': 41.6831, 'saleRate': 43.15, 'purchaseRate': 41.28}, {'baseCurrency': 'UAH', 'currency': 'CNY', 'saleRateNB': 5.021, 'purchaseRateNB': 5.021}, {'baseCurrency': 'UAH', 'currency': 'CZK', 'saleRateNB': 1.6548, 'purchaseRateNB': 1.6548, 'saleRate': 1.715, 'purchaseRate': 1.6425}, {'baseCurrency': 'UAH', 'currency': 'DKK', 'saleRateNB': 5.3464, 'purchaseRateNB': 5.3464}, {'baseCurrency': 'UAH', 'currency': 'EUR', 'saleRateNB': 39.8415, 'purchaseRateNB': 39.8415, 'saleRate': 41.85, 'purchaseRate': 40.85}, {'baseCurrency': 'UAH', 'currency': 'GBP', 'saleRateNB': 46.6688, 'purchaseRateNB': 46.6688, 'saleRate': 48.37, 'purchaseRate': 46.28}, {'baseCurrency': 'UAH', 'currency': 'GEL', 'saleRateNB': 13.9272, 'purchaseRateNB': 13.9272}, {'baseCurrency': 'UAH', 'currency': 'HUF', 'saleRateNB': 0.103418, 'purchaseRateNB': 0.103418}, {'baseCurrency': 'UAH', 'currency': 'ILS', 'saleRateNB': 9.6968, 'purchaseRateNB': 9.6968}, {'baseCurrency': 'UAH', 'currency': 'JPY', 'saleRateNB': 0.25075, 'purchaseRateNB': 0.25075}, {'baseCurrency': 'UAH', 'currency': 'KZT', 'saleRateNB': 0.079125, 'purchaseRateNB': 0.079125}, {'baseCurrency': 'UAH', 'currency': 'MDL', 'saleRateNB': 2.0664, 'purchaseRateNB': 2.0664}, {'baseCurrency': 'UAH', 'currency': 'NOK', 'saleRateNB': 3.4647, 'purchaseRateNB': 3.4647}, {'baseCurrency': 'UAH', 'currency': 'PLN', 'saleRateNB': 8.9074, 'purchaseRateNB': 8.9074, 'saleRate': 9.23, 'purchaseRate': 8.83}, {'baseCurrency': 'UAH', 'currency': 'SEK', 'saleRateNB': 3.3572, 'purchaseRateNB': 3.3572}, {'baseCurrency': 'UAH', 'currency': 'SGD', 'saleRateNB': 26.9322, 'purchaseRateNB': 26.9322}, {'baseCurrency': 'UAH', 'currency': 
'TMT', 'saleRateNB': 10.4482, 'purchaseRateNB': 10.4482}, {'baseCurrency': 'UAH', 'currency': 'TRY', 'saleRateNB': 1.3494, 'purchaseRateNB': 1.3494}, {'baseCurrency': 'UAH', 'currency': 'UAH', 'saleRateNB': 1.0, 'purchaseRateNB': 1.0}, {'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 36.5686, 'purchaseRateNB': 36.5686, 'saleRate': 38.0, 'purchaseRate': 37.4}, {'baseCurrency': 'UAH', 'currency': 'UZS', 'saleRateNB': 0.0031524, 'purchaseRateNB': 0.0031524}, {'baseCurrency': 'UAH', 'currency': 'XAU', 'saleRateNB': 69443.04, 'purchaseRateNB': 69443.04}]}

class CurrencyRatePrinter:
    @staticmethod
    def print_currency_rate(currency, data):
        rate = None
        for entry in data['exchangeRate']:
            if entry['currency'] == currency:
                rate = entry
                break

        if rate:
            print(f"Курс {currency}: {rate['saleRate']} (продажа) / {rate['purchaseRate']} (покупка)")
        else:
            print(f"Курс {currency} не найден.")


CurrencyRatePrinter.print_currency_rate('USD', data)
CurrencyRatePrinter.print_currency_rate('EUR', data)
