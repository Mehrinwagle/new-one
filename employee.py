class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary 
        self.gender=gender
    def emp_details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary",self.salary)
        print("gender",self.gender)

p1=Employee("Ram",25,10000,"Male")
p1.emp_details()