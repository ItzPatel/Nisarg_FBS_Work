#Write a program to calculate the percentage of student based on marks of any 5 subjects.
eng = int(input("Enter marks in English: "))
math = int(input("Enter marks in Math: "))
science = int(input("Enter marks in Science: "))    
social_studies = int(input("Enter marks in Social Studies: "))
hindi = int(input("Enter marks in Hindi: "))

total_marks = eng + math + science + social_studies + hindi

percentage = (total_marks / 500) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")