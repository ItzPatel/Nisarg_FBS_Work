#Convert distant given in feet and inches into meter and centimeter.
feet = int(input("Enter the distance in feet:"))
inch = int(input("Enter the distance in inches:"))

total_meters = (feet * 0.3048) + (inch * 0.0254)

meters = int(total_meters)
centimeters = (total_meters - meters) * 100

print(f"\nDistance in meters: {meters} m")
print(f"Distance in centimeters: {centimeters:.2f} cm") 