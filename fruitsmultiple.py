#list .
class Fruits:
    def name(self,a):
        self.a=a

class Cost:
    def price(self,b):
        self.b=b
        
class Basket(Fruits,Cost):
    def show(self):
        print(self.a)
        print(self.b)
    

enter=int(input("enter the number of list :"))
Mylist=[]
Costlist=[]
for i in range(enter):
    c=input("enter the fruits name :")
    Mylist.append(c)
    b=input("enter cost of fruits :")
    Costlist.append(b)
d=Basket()
d.name(Mylist)
d.price(Costlist)
d.show()