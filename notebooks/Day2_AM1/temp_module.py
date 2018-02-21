absolute_zero_in_celsius = -273.15

def fahrenheit_to_kelvin(temperature):
    """This function turns a temperature in Fahrenheit into a temperature in Kelvin"""
    return (temperature - 32) * 5/9 - absolute_zero_in_celsius

def kelvin_to_celsius(temperature):
    """This function turns a temperature in Kelvin into a temperature in Celsius
    
    This string is a doc string. It uses triple quotes to allow line breaks and contains information about your function that is carried around. You can access it by calling help(function) for any function that provides it. May editors will also show it if you hover over the function."""
    return temperature + absolute_zero_in_celsius

def fahrenheit_to_celsius(temperature):
    temp_in_kelvin = fahrenheit_to_kelvin(temperature)
    return kelvin_to_celsius(temp_in_kelvin)

absolute_zero_in_fahrenheit = fahrenheit_to_celsius(absolute_zero_in_celsius)

# The magic variable __name__ contains the name of the module.
# If the file is run as a script it instead is set to "__main__"
# print(f"You have loaded the module {__name__}")
