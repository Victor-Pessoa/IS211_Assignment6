import conversions.py

def test_celsius_to_fahrenheit():
    # Test cases for celsius to fahrenheit conversion
    assert round(conversions.convertCelsiusToFahrenheit(0), 2) == 32.00
    assert round(conversions.convertCelsiusToFahrenheit(100), 2) == 212.00
    assert round(conversions.convertCelsiusToFahrenheit(-40), 2) == -40.00

def test_fahrenheit_to_celsius():
    # Test cases for fahrenheit to celsius conversion
    assert round(conversions.convertFahrenheitToCelsius(32), 2) == 0.00
    assert round(conversions.convertFahrenheitToCelsius(212), 2) == 100.00
    assert round(conversions.convertFahrenheitToCelsius(-40), 2) == -40.00

def test_celsius_to_kelvin():
    # Test cases for celsius to kelvin conversion
    assert round(conversions.convertCelsiusToKelvin(0), 2) == 273.15
    assert round(conversions.convertCelsiusToKelvin(100), 2) == 373.15
    assert round(conversions.convertCelsiusToKelvin(-273.15), 2) == 0.00

def test_kelvin_to_celsius():
    # Test cases for kelvin to celsius conversion
    assert round(conversions.convertKelvinToCelsius(273.15), 2) == 0.00
    assert round(conversions.convertKelvinToCelsius(373.15), 2) == 100.00
    assert round(conversions.convertKelvinToCelsius(0), 2) == -273.15

def test_fahrenheit_to_kelvin():
    # Test cases for fahrenheit to kelvin conversion
    assert round(conversions.convertFahrenheitToKelvin(32), 2) == 273.15
    assert round(conversions.convertFahrenheitToKelvin(212), 2) == 373.15
    assert round(conversions.convertFahrenheitToKelvin(-40), 2) == 233.15

def test_kelvin_to_fahrenheit():
    # Test cases for kelvin to fahrenheit conversion
    assert round(conversions.convertKelvinToFahrenheit(273.15), 2) == 32.00
    assert round(conversions.convertKelvinToFahrenheit(373.15), 2) == 212.00
    assert round(conversions.convertKelvinToFahrenheit(233.15), 2) == -40.00

if __name__ == "__main__":
    # Run all the conversion tests
    test_celsius_to_fahrenheit()
    test_fahrenheit_to_celsius()
    test_celsius_to_kelvin()
    test_kelvin_to_celsius()
    test_fahrenheit_to_kelvin()
    test_kelvin_to_fahrenheit()
    
    print("All conversion tests passed!")
