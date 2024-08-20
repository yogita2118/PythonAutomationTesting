"""
Task #2
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""

Number1 = int(input("Enter the num1 :"))
Number2 = int(input("Enter the numb2 :"))

print("Maximum numb of "f"{Number1} , "f"{Number2} is :" , max(Number1, Number2))

print("Power value of "f"{Number1} , "f"{Number2} is :", pow(Number1,Number2))

print("Sum of "f"{Number1} , "f"{Number2} is:", Number1+Number2)
print("Mul of "f"{Number1} , "f"{Number2} is:", Number1*Number2)
print("Sub of "f"{Number1} , "f"{Number2} is:", Number1-Number2)
print("Div of"f"{Number1} , "f"{Number2} is:", Number1/Number2)


