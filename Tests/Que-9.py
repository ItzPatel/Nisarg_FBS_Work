#(Test - 2) A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST. Use python and solve the code

product1 = float(input("Enter the price of product 1: "))
product2 = float(input("Enter the price of product 2: "))
product3 = float(input("Enter the price of product 3: "))
product4 = float(input("Enter the price of product 4: "))
product5 = float(input("Enter the price of product 5: "))

total = product1 + product2 + product3 + product4 + product5
gst = total * 0.18
total_bill = total + gst

print("Total bill after adding 18% GST is:", total_bill)