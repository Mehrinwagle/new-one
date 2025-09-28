 # method Overiding - class Animal:
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):   # Overrides Animal.speak
        print("Dog barks")

a = Animal()
d = Dog()

a.speak()  # Animal makes a sound
d.speak()  # Dog barks   <-- Child method overrides parent method