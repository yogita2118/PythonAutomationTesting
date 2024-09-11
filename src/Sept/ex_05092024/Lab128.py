# Multiple Inheritance

class Father:
    key = "ABC"
    __password = "private"

    def __show_password(self):
        print(self.__password)
    def father_money(self):
        return 5
    def home(self):
        return "This is from the Father"

    def show_everything(self):
        self.__show_password()

class Mother:
    def mother_money(self):
        return 2
    def home(self):
        return "This is from the Mother"

class Son(Father,Mother):
    pass

s = Son()
print(s.mother_money())
print(s.father_money())
print(s.home())
print(s.key)
s.show_everything()

