#multiple inheritence
class First:
    def one(self,int1):
        self.int1=int1
    
class Second:
    def two(self,int2):
        self.int2=int2
  
class Third(First,Second):
    def math(self,add,result):
        self.add=add
        self.result=result
        if self.add == '+':
            self.result= self.int1 + self.int2
            print(self.result)
        else:
            print("error")
        


int1=int(input("enter first value : "))
int2=int(input("enter second value : "))
cal=input("enter which operation you want : ")
d=Third()
d.one(int1)
d.two(int2)
d.math(cal,int)