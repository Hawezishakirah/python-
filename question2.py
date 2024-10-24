# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

def get_grades(marks):
    grades = float(input("enter the grades"))

    if marks >="90%":
        return("A")
    elif marks >="80%":
     return("B")
    elif marks >="70%":
     return("C")
    elif marks >="60%":
     return("D")
    elif marks >="40%":
     return("E")
    else:
     return"invalid marks"
marks = float(input("Enter the student's marks from (0-90)"))

grade = get_grades(marks)
print(f"the student's grade is:{grade}")