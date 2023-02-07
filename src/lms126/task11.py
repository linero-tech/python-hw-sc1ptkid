from to_do import TODO


def task11():
    return """
# Convert Celsius to Fahrenheit

START
INPUT celsius value
    IF value is a integer
    Calculate fahrenheit_value = (Celsius_value * 9/5) + 32
OUTPUT print Fahrenheit_value
END

# Convert Fahrenheit to Celsius

START
INPUT Fahrenheit value
    IF value is a integer
    Calculate Celsius_value = (Fahrenheit_value - 32) * 5/9
OUTPUT print Celsius_value
END 

"""