class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def display_info(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee ID : {self.emp_id}")
        
class Manager(Employee):
    def __init__(self, name, emp_id, deparment):
        super().__init__(name, emp_id)
        self.deparment = deparment
    def display_info(self):
        super().display_info()
        print(f"Employee department {self.deparment}")
        
class Developer(Employee):
    def __init__(self, name, emp_id, programming):
        super().__init__(name, emp_id)
        self.prog_lang = programming
    def display_info(self):
        super().display_info()
        print(f"Developer coding language : {self.prog_lang}")
        
        
obj1 = Manager("hemant", 123, "management")
obj1.display_info()
obj2 = Developer("ashish", 312, "Python")
obj2.display_info()