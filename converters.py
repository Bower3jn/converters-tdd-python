""" library of units converters """

"""
    This is a program that can convert
    GBP into USD
"""
def gbp2usd(gbp):
    """"
        Converts GBP to USD using the formula:
        GBP * 1.5936
    """
    return gbp * 1.5936

# ask the user to input GBP value
gbp = input("what is the GBP? ")
#convert the input in to a numeric (float value)
gbp = float(gbp)
print(gbp * 1.5936)
