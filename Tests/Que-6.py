#(Test-2)Write a program to accept 3 digit number. If first digit is double of second digit and half of
#third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
#Eg : - 428 , 214 etc.

num = int(input("Enter a three digit number:"))

if(len (str(num)) == 3):
    first = int(str(num)[0])
    second = int(str(num)[1])
    third = int(str(num)[2])
    
if (first == 2 * second) and (first == third / 2):
    print("Yes, you have done it")
else:
    print("Please try next time")