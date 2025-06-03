# Create a phone number keypad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for numbers in num_pad:
    for number in numbers:
        print(number, end=" ")
    print()

