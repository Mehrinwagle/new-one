# base class
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_v_details(self):
        print("mileage of vehicle is:",self.mileage)
        print("cost of vehicle is:",self.cost)
        print("i am a vehicle")
v1=Vehicle(500,10000)
v1.show_v_details()
# child class
class Car(Vehicle):
    def __init__(self,mileage,cost,tyre,hp):
        super().__init__(mileage,cost)
        self.tyre=tyre
        self.hp=hp
    def show_car_details(self):
        print("no. of tyre in the car:",self.tyre)
        print("horse power of the car is :",self.hp)
        print("i am a car")
c1=Car(600,10000,4,500)
c1.show_car_details()
c1.show_v_details()