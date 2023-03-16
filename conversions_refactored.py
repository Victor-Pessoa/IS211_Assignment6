class ConversionNotPossible(Exception):
    pass

def convert_celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convert_miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

def convert_yards_to_meters(yards):
    meters = yards * 0.9144
    return meters

def convert_meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

def convert(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return convert_celsius_to_kelvin(value)
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return convert_celsius_to_fahrenheit(value)
    elif from_unit == "Miles" and to_unit == "Kilometers":
        return convert_miles_to_kilometers(value)
    elif from_unit == "Yards" and to_unit == "Meters":
        return convert_yards_to_meters(value)
    elif from_unit == "Meters" and to_unit == "Feet":
        return convert_meters_to_feet(value)
    else:
        raise ConversionNotPossible(f"Conversion from {from_unit} to {to_unit} is not possible.")
