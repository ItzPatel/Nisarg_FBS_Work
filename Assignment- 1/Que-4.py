#Write a program to enter P, T, R and calculate simple Interest.
P = float(input("Enter Principal amount (P): "))
T = float(input("Enter Time in years (T): "))
R = float(input("Enter Rate of interest (R): "))

SI= P*R*T/100

print("Simple Interest is:", SI)