""" library of units converters """

"""
This is a program that can convert
GBP into USD
"""
# Declaring Known constsnta
GBP = 1            #base
USD = (GBP) * 1.5936 #converstion rate

def gbp2usd(gbp):
    """"
        Converts GBP to USD using the formula:
        GBP * conversion rate
    """
    return gbp * 1.2953716257

# ask the user to input GBP value
gbp = input("what is the GBP? ")
#convert the input in to a numeric (float value)
gbp = float(gbp)
print(round(gbp2usd(gbp), 2), "usd")
