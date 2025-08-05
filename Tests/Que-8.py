#Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.
h = int(input("Enter the height:"))
w = int(input("Enter the width:"))
cost_per_sq_meter = int(input("Enter the cost per sq meter:"))

total_area = 4 * h * w
total_cost = total_area * cost_per_sq_meter

print("Total cost of painting the interior of the building is:", total_cost)