#multi-level inheritance
class Parent:
    def one(self):
        print("this is the parent ")

class Child(Parent):
    def two(self):
        print("this is child")

class Grandchild(Child):
    def three(self):
        print("this is grandchild")

c=Grandchild()
c.one()
c.two()
c.three()