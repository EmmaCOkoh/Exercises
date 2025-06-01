
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

# Celsius to Fahrenheit = (celsius°C × 9/5) + 32 = °F
# Fahrenheit to Celsius = (fahrenheit°F − 32) × 5/9 = °C

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    unit = "°F"
    print(f"The temperature in Fahrenheit is : {temp}{unit}")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = "°C"
    print(f"The temperature in Celsius is : {temp}{unit}")
else:
    print(f"{unit} is an invalid unit of measurement")