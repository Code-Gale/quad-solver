import math

print("Waddup, Let's solve some quads")
print("--------------------------------")

# Gather coefficients from the user
coef_a = float(input("Enter the coefficient of (a): "))
coef_b = float(input("Enter the coefficient of (b): "))
coef_c = float(input("Enter the coefficient of (c): "))

print()
print(f"Solving your problem: {coef_a}x^2 + {coef_b}x + {coef_c} = 0")

# Calculate the discriminant
discriminant = coef_b**2 - 4*coef_a*coef_c

if discriminant > 0:
    # Two distinct real solutions
    sol1 = (-coef_b + math.sqrt(discriminant)) / (2*coef_a)
    sol2 = (-coef_b - math.sqrt(discriminant)) / (2*coef_a)
    print(f"There are two precise real solutions: {sol1} and {sol2}")

elif discriminant == 0:
    # One real solution (double root)
    sol = -coef_b / (2*coef_a)
    print(f"There is one precise solution (double root): {sol}")

else:
    # Two complex solutions
    real_part = -coef_b / (2*coef_a)
    imaginary_part = math.sqrt(-discriminant) / (2*coef_a)
    print(f"There are two complex solutions: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

print("Done and Dusted!")
