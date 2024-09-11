# Inheritance


class Father:
    key = "2BHK"   # Attributes

    def car(self): # Behaviour
        print("Father Car!!", "ALTO")

class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Truck")

father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.car()