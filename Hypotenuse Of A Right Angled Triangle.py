# Hypotenuse of a right angled triangle
# c = √(a² + b²)

import math

a = float(input(f"That is the number on side a?: "))
b = float(input(f"That is the number on side b?: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side c is equal to {round(c, 2)}cm")
