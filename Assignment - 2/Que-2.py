#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
cel = float(input("Enter temperature in Celsius: "))
far = (9/5) * cel +32 

print(f"\nTemperature in Fahrenheit: {far:.2f}")