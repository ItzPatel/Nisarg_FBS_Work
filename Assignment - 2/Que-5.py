#WAP to calculate selling price of book based on cost price and discount.
cp = int(input("Enter the cost price of the book:"))
dis = float(input("Enter the discount for the book:"))

dis_amt = (dis / 100) * cp
sp = cp - dis_amt

print("Selling Price of the book =", round(sp, 2))