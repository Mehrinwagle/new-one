class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_vehicledetails(self):
        print("mileage:",self.mileage)
        print("cost:",self.cost)
        print("i am a vehicle")
class Car(Vehicle):
    def show_cardetails():
        print("i am a car")
    
c1=Car(250,1000)
c1.show_vehicledetails()
