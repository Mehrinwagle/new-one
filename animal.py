#call the parent class method
class Animal:
    def speak(self):
        print("animal makes a sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("dog barks")

d=Dog()
d.speak()