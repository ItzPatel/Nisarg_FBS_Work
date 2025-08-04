# Write a Program to input two angles from user and find third angle of the triangle.
ang1 = float(input("Enter first angle: "))
ang2 = float(input("Enter second angle: "))

ang3 = 180 - (ang1 + ang2)

print("The third angle is:", ang3)