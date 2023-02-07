from to_do import TODO


def task11():
    return """
# Convert Celsius to Fahrenheit

START
INPUT Celsius_value
    IF value is a integer
    Calculate Fahrenheit_value = (Celsius_value * 9/5) + 32
OUTPUT print Fahrenheit_value
END

# Convert Fahrenheit to Celsius

START
INPUT Fahrenheit_value
    IF value is a integer
    Calculate Celsius_value = (Fahrenheit_value - 32) * 5/9
OUTPUT print Celsius_value
END 

"""