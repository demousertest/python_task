import random
class Employees:

    def employee_details(self,number_of_emp):
        locations = ['Kormangala', 'HSR Layout', 'Ballary', 'Mumbai', 'Chennai', 'Nellore', 'Gurgon', 'Hyderabad']
        for i in range(number_of_emp):
            salary = random.randint(20000, 150000)
            location = random.choice(locations)
            emp_id = random.randint(1,9999)

            yield{
                "Emp id" : emp_id,
                'Emp location' : location,
                "Emp Salary"    : salary
            }

    def fetch_details(self):
        num_of_emp = int(input("Enter number of employee records : "))
        test = self.employee_details(num_of_emp)
        for i in test:
            print(i, end="\n")

obj = Employees()
obj.fetch_details()