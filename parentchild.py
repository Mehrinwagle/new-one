# parent class one
class Parent_1:
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        print(self.str1)
# parent class two
class Parent_2:
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        print(self.str2)
# child class
class Derived(Parent_1,Parent_2):
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        print(self.str3)
d=Derived()
d.assign_string_one("one")
d.assign_string_two("one")
d.assign_string_three("one")
d.show_string_one()
d.show_string_two()
d.show_string_three()