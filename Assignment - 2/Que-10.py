#Write a program to reverse three-digit number.
num = int(input("Enter the three-digit number: "))

d1 = num % 10
d2 = (num// 10) %10
d3 = num // 100

rev_num = d1*100 + d2*10 + d3
print(f"Reversed number: {rev_num}")