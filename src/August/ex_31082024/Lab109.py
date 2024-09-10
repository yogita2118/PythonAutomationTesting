# Constructor
# Special Function in Class,  __init__()
# It will be automatically called when you create an Object

class Dog:
    name = None

    def __init__(self):
        print("I will be automatically called when you create an Object")

    def sleep(self):
        print("Sleeping")

dog1 = Dog()