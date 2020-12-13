# Converts degress Fahrenheit to degress Celcius
def f2c(fahrenheit) :
    """
    Converts degrees Fahrenheit to degrees Celsius using the formual:
    T(c)= (T(f)-32) /(9/5)
    """
    #ask user to input tempeture in farenheit
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

#converts degrees Celcius to degress Fahrenheit
def c2f(celcius) :
    """
    Converts degrees Celsius to degrees Fahrenheit using the formual:
    T(f)= T(c)*1.8 + 32
    """
    #ask user to input temperture in celcius
    celcius = float(input("Enter temperature in celcius: "))
    fahrenheit = ((1.8)* celcius) + 32
    print('%.2f Celcius is: %0.2f Fahrenheit' %(celcius, fahrenheit))
