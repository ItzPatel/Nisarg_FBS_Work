#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter the amount in rupees: "))
temp = amount

two_thousand = temp // 2000
temp = temp % 2000

five_hundred = temp // 500
temp = temp % 500

two_hundred = temp // 200
temp = temp % 200

one_hundred = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

five = temp // 5
temp = temp % 5

one = temp // 1
temp = temp % 1

print(f"2000s: {two_thousand}, 500s: {five_hundred}, 200s: {two_hundred}, 100s: {one_hundred}, 50s: {fifty}, 20s: {twenty}, 10s: {ten}, 5s: {five}, 1s: {one}")