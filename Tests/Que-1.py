l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
r = float(input("Enter the radius of the circle: "))

pi = 3.14

area_rectangle = l * b
area_semi_circle = 0.5 * pi * r * r
total_area = area_rectangle + area_semi_circle

perimeter = 2 * l + b + pi * r

print(f"The Area is: {total_area}")
print(f"The Perimeter is: {perimeter}")