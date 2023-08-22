rates={ 
     "USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
    "BAM": 1.7974
    }

# currency exchange rate application




from json import load
with open("C:\Users\Arya\Desktop\mypythonprograms\currencyexchange\db.json") as f:
    data=load(f)

rates=data.get("conversion_rates")
amount=int(input("enter amount>"))
fromcurrencycode=input("enter source currency code>")
tocurrencycode=input("enter destination currency code :>")

from_rate=rates.get(fromcurrencycode)
to_rate=rates.get(tocurrencycode)

 