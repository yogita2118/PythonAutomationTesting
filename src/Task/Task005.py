"""
Task #5
- Create a program that takes two numbers as input and
prints whether the first number is greater than, less than, or equal to the second number.
"""
Num1 = int(input("Enter the number1 :" ))
Num2 = int(input("Enter the number2 :"))

if(Num1 > Num2):
    print(" "f"{Num1} is greater than {Num2} ")
elif(Num1 < Num2):
    print(" "f"{Num1} is less than {Num2}")
else:
    print(" "f"{Num1} is equal to {Num2}")