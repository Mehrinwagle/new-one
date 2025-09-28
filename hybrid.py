#hybrid inheritance
#base class
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name",self.name)
#derived class 1(single inheritance)
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
    def show_employee(self):
        print("Emp_id",self.emp_id)
#derived class 2(multiple inheritance)
class Admin(Employee):
    def __init__(self,name,emp_id,role):
        super().__init__(name,emp_id)
        self.role=role
    def show_role(self):
        print("role",self.role)
#another base class(hireachal part)
class Contact:
    def __init__(self,email):
        self.email=email
    def show_email(self):
        print("email",self.email)
#hybrid inheritance: admin contact inherits from admin and contact(multiple+multilevel)
class AdminContact(Admin,Contact):
    def __init__(self,name,emp_id,role,email):
        Admin.__init__(self,name,emp_id,role)
        Contact.__init__(self,email)
    def show_details(self):
        self.show_name()
        self.show_employee()
        self.show_role()
        self.show_email()
        
d=AdminContact("priya",23,"manager","abc@gmail.com")
d.show_details()