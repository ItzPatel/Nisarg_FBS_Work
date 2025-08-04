#Find the sum of three-digit number.
num1 = int(input("Enter the three-digit number: "))
temp = num1

d = num1 % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

sum = d + d2 + d3
print(f"Sum of digits: {sum}")