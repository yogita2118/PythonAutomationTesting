class Parent:
    gold = "2Kg"

    def BHK3(self):
        print("3BHK")

class Child(Parent):
    diamond = "Diamond"

    def BHK2(self):
        print("2BHK")

child_object = Child()
print(child_object.gold)
child_object.BHK3()
child_object.BHK2()

father_object_ref = Parent()
father_object_ref.BHK3()
# father_object_ref.BHK2() 
#print(father_object_ref.diamond)
