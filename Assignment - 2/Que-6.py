#WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
basic_salary = int(input("Enter basic salary: ₹"))

da = 0.10 * basic_salary  
hra = 0.15 * basic_salary 
ta = 0.12 * basic_salary 

total_salary = basic_salary + da + hra + ta

print("\n Salary Breakdown:")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"DA (10%): {da:.2f}")
print(f"HRA (15%): {hra:.2f}")
print(f"TA (12%): {ta:.2f}")
print(f"Total Salary: {total_salary:.2f}")