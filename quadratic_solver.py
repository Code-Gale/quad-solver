import math

print("Waddup, Shall we begin?")
print("------------------------------------------------")

while True:
    try:
        a_coefficient = float(input("Give me the 'a' coefficient: "))
        b_coefficient = float(input("How about the 'b' coefficient: "))
        c_coefficient = float(input("Lastly, the 'c' coefficient: "))
        break  # Exit the loop if all inputs are valid
    except ValueError:
        print("Oops! That's not a valid number. Please try again.")

print()
print(f"Alright, lets begin: {a_coefficient}x^2 + {b_coefficient}x + {c_coefficient} = 0")

discriminant = b_coefficient**2 - 4*a_coefficient*c_coefficient

if discriminant > 0:

    sol1 = (-b_coefficient + math.sqrt(discriminant)) / (2*a_coefficient)
    sol2 = (-b_coefficient - math.sqrt(discriminant)) / (2*a_coefficient)
    print(f"Done! Two precise real solutions: {sol1} and {sol2}")

elif discriminant == 0:
    sol = -b_coefficient / (2*a_coefficient)
    print(f"Looks like we have a single precise solution (double root): {sol}")

else:
    real_part = -b_coefficient / (2*a_coefficient)
    imaginary_part = math.sqrt(-discriminant) / (2*a_coefficient)
    print(f"We've got two complex solutions for this: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

print("Done and dusted!")
