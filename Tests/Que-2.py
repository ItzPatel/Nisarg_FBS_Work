principal_amt = int(input("Enter the principal amount: "))
roi = float(input("Enter the rate of interest (in %): "))
time = int(input("Enter the time (in years): "))

cal_SI = (principal_amt * roi * time) / 100

print(f"The Simple Interest is: {cal_SI}")