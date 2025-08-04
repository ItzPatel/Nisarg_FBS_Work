#Write a program to convert days into years, weeks and days.
days = int(input("Enter number of days: "))

yrs =  days // 365
weeks = (days % 365) // 7
remain_days = (days % 365) % 7

print("Years:", yrs)
print("Weeks:", weeks)
print("Remaining Days:", remain_days)