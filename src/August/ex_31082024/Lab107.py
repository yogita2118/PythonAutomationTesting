class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    # def means creating a function
    # Self means this, self will be first argument in every behaviour.
    def talk(self):
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a method! !")
        print("Sleep", name)

    def walk(self):
        print("I am walking")

    def walk_return(self):  # No Arg with Return
        return "I am walking"


# Create an Object of the Class
# ObjectRef = ClassName() -> Object

tushar = Person()
tushar.name = "tushar"
print(tushar.name)

hiva = Person()
hiva.name = "hiva"
print(hiva.name)