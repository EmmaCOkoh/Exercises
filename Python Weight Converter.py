# Python weight converter

try:
    weight = float(input("Enter your weight: "))
    unit = input("Kilograms or Pounds (kg or lb): ")

    if unit == "kg":
        weight = 1 * 2.20462
        unit = "Lbs"
        print(f"Your weight is {round(weight, 1)} {unit}")
    elif unit == "lb":
        weight = 1 * 0.453592
        unit = "Kgs"
        print(f"Your weight is {round(weight, 1)} {unit}")
    else:
        print("Invalid input")
except ValueError:
    print("Please enter a valid numeric weight (e.g., 70.5).")





