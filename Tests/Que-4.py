area = float(input("Enter the area of one wall: "))
int_cost_per_unit = float(input("Enter the interior painting cost per unit area: "))
ext_cost_per_unit = float(input("Enter the exterior painting cost per unit area: "))

int_walls = 8
ext_walls = 6

int_total = int_walls * area * int_cost_per_unit
ext_total = ext_walls * area * ext_cost_per_unit
total_cost = int_total + ext_total

print("Interior painting cost:", int_total)
print("Exterior painting cost:", ext_total)
print("Total painting cost:", total_cost)