# First parent class
class Father:
    def skill_father(self,val1):
        self.val1=val1

# Second parent class
class Mother:
    def skill_mother(self,val2):
        self.val2=val2
        

# Child class inherits from BOTH Father and Mother
class Child(Father, Mother):
    def skill_child(self,op,result):
        self.op=op
        self.result=result
        if self.op == "+":
            self.result=self.val1+self.val2
            print(self.result)
        else:
            print("Error")


x=int(input("Enter 1st value"))
y=int(input("Enter 2nd value"))
z=input("Enter mode of opertion, e.g. '+' ")

# Create object of Child
c = Child()

# Object c can use methods from BOTH parents
c.skill_father(x)   # From Father
c.skill_mother(y)
c.skill_child(z,int)    # From Child
