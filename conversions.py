def convertCelsiusToKelvin(celsius):
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    return (celsius * 1.8) + 32

def convertFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def convertFahrenheitToKelvin(fahrenheit):
    return convertCelsiusToKelvin(convertFahrenheitToCelsius(fahrenheit))

def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15

def convertKelvinToFahrenheit(kelvin):
    return convertCelsiusToFahrenheit(convertKelvinToCelsius(kelvin))

