# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount:$ "))
    if principle <= 0:
        print("Sorry principle can't be less or equal to 0")
while rate <= 0:
    rate = float(input("Enter the rate in percentage:% "))
    if rate <= 0:
        print("Sorry rate can't be less or equal to 0")
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Sorry time can't be less or equal to 0")

print(f"Your initial principle balance is ${round(principle, 2)}")
print(f"Your interest rate is {rate}%")
print(f"Your number of time is {time}")

final_amount = principle * pow((1 + rate / 100), time)
print(f"The final amount after {time} year/s: ${final_amount:.2f}")

