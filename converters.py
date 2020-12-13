"""Library of units converters"""

# Declare useful constants
MI  = 0.621371   # miles per km
KM  = 1.609344   # km per mile
G   = 28.34953   # grams per onunce
OZ  = 0.035274   # Ounces per gram


def mi2km(miles):
    """
    Takes in Miles value and converts it to Kilometers.
    """
    #ask user to input value for miles
    miles = float(input("Enter distance in miles: "))
    kilometer = (miles * 1.609344)
    print('%.2f Miles is: %0.2f Kilometers' %(miles, kilometer))

def km2mi(kilometer):
    """
    Takes in a Kilometer value and converts it to miles.
    """
    #ask user to input value for miles
    kilometer = float(input("Enter distance in Kilometers: "))
    miles = (kilometer *  0.621371)
    print('%.2f kilometers is: %0.2f miles' %(kilometer, miles))

def g2oz(grams):
    """
    Takes in value for Grams and converts it to Ounces.
    """
    #ask user to input value for grams
    grams = float(input("Enter mass in Grams: "))
    ounces = (grams *  0.035274)
    print('%.2f Grams is: %0.2f Ounces' %(grams, ounces))

def oz2g(ounces):
    """
    Takes in Ounces value and converts it to Grams.
    """
    ounces = float(input("Enter mass in Ounces: "))
    grams = (ounces *  28.34953)
    print('%.2f Ounces is: %0.2f Grams' %(ounces, grams))

