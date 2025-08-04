#WAP to calculate area of triangle and rectangle
base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
area_tri = 0.5 * base * height
print(f"The area of triangle is: {area_tri:.2f}")

length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
area_rect = length * width
print(f"The area of rectangle is: {area_rect:.2f}")