#Write a program to enter P, T, R and calculate Compound Interest.
P = float(input("Enter Principal amount (P): "))
T = float(input("Enter Time in years (T): "))
R = float(input("Enter Rate of interest (R): "))

CI = P * (1 + R / 100) ** T - P

print("Compound Interest is:", CI)
