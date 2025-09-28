# First parent class
class Father:
    def skill_father(self):
        print("Father knows driving.")

# Second parent class .
class Mother:
    def skill_mother(self):
        print("Mother knows cooking.")

# Child class inherits from BOTH Father and Mother
class Child(Father, Mother):
    def skill_child(self):
        print("Child knows painting.")

# Create object of Child
c = Child()

# Object c can use methods from BOTH parents
c.skill_father() # From Father
c.skill_mother() # From Mother
c.skill_child() # From Child