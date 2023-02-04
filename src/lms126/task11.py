from to_do import TODO


def task11():
    return """
# Convert Celsius to Fahrenheit

START
INPUT celsius value
SET fahrenheit_value = (Celsius_value * 9/5) + 32
DISPLAY print Fahrenheit_value
END

# Convert Fahrenheit to Celsius

START
INPUT Fahrenheit value
SET Celsius_value = (Fahrenheit_value - 32) * 5/9
DISPLAY print Celsius_value
END 

"""