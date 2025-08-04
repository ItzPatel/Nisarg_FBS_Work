#Program to Find the Roots of a Quadratic Equation
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c

rt1 = (-b + D**0.5) / (2*a)
rt2 = (-b - D**0.5) / (2*a)

print("Root 1 is:", rt1)
print("Root 2 is:", rt2)