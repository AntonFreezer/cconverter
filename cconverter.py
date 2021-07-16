import requests
import json


currency_rates = {}
cache = {}


def requesting(currency):
    global currency_rates
    r = requests.get(f"http://www.floatrates.com/daily/{currency.lower()}.json")
    currency_rates = json.loads(r.text)


def caching_base():
    if "usd" in currency_rates:
        cache["usd"] = currency_rates["usd"]['rate']
    if "eur" in currency_rates:
        cache["eur"] = currency_rates["eur"]['rate']


def main():
    initial_currency = input("What's your currency?\n")
    if initial_currency != """""":
        requesting(initial_currency)
        caching_base()
        while True:
            currency_to_receive = input("What currency you wish to receive?\n").lower()
            if currency_to_receive != """""":
                money_amount = float(input("How much money have you got?\n"))
                print('Checking the cache...')
                if currency_to_receive in cache:
                    print("Oh! It is in the cache!")
                    received_amount = money_amount * cache[currency_to_receive]
                    print(f"You received {round(received_amount, 2)} {currency_to_receive.upper()}")
                else:
                    print("Sorry, but it is not in the cache!")
                    cache[f"{currency_to_receive}"] = currency_rates[f"{currency_to_receive}"]['rate']
                    received_amount = money_amount * cache[currency_to_receive]
                    print(f"You received {round(received_amount, 2)} {currency_to_receive.upper()}")
            else:
                break


main()
