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
    def skill_child(self):
        print(self.val1+self.val2)

# Create object of Child
c = Child()

# Object c can use methods from BOTH parents
c.skill_father(5)   # From Father
c.skill_mother(10)   # From Mother
c.skill_child()    # From Child