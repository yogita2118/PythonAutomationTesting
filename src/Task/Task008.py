"""
Task #8
✅ Triangle Classifier:
![img.png](img.png)
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""

Side1 = int(input("Enter the value of side1 :"))
Side2 = int(input("Enter the value of side2 :"))
Side3 = int(input("Enter the value of side3 :"))

if Side1 == Side2 == Side3 :
    print("It is a Equilateral")
elif Side1 == Side2 != Side3 :
    print("It is a Isosceles")
else:
    print("It is a Scalene")


