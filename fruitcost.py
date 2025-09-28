#list 
class Fruits:
    def __init__(self,Mylist,a,costlist,b):
        self.Mylist=[]
        self.costlist=[]
        self.a=a
        self.b=b
    def name(self):
        for i in range(3):
            self.a=input("enter name :")
            self.Mylist.append(self.a)
    def price(self):
        for j in range(3):
            self.b=int(input("enter cost :"))
            self.costlist.append(self.b)
class Basket(Fruits):
    def show(self):
        for n in self.Mylist:
            print(n)
    def show_1(self):
        for m in self.costlist:
            print(m)

d=Basket(list,str,list,int)
d.name()
d.price()
d.show()
d.show_1()

