
from requests import get
def convert(amount: float, target: str = "GBP" , base: str = "USD") :
    """
    Function to convert "value"  of base currency in to target currency
    """
    # Get URL to pass exchange rates URL
    url = 'https://api.exchangeratesapi.io/latest?base=%s&symbols=%s' % (base, target)
    # request exchange rates responce
    responce = get(url)
    # extract the JSON data 
    data = responce.json()
    # extract conversion factor
    factor = data['rates'][target]
    # return the converted value
    return f"{amount} {base} is {round(amount * factor, 2)} {target}"

b = input('What currency do you want to convert from? ')
t = input('What currency do you want to convert to? ')
amt = input('How much do you wan to convert? ')
print(convert(float(amt), t.upper(), b.upper()))
