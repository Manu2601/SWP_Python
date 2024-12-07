class Person():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
class Employee(Person):
    def __init__(self, name, gender):
        super().__init__(name=name, gender=gender)
        
class Departmentmanager(Employee):
    def __init__(self, name, gender):
        super().__init__(name=name, gender=gender)
        
class Department():
    def __init__(self, name, departmentmanager, employees):
        self.name = name
        self.departmentmanager = departmentmanager
        self.employees = employees
        
class Company():
    def __init__(self, name, department):
        self.name = name
        self.departments = department
        
    def countemployees(self):
        count = 0
        for department in self.departments:
            count += len(department.employees)
        return count
    
    def countdepartmentmanager(self):
        count = 0
        for department in self.departments:
            if isinstance(department.departmentmanager, Departmentmanager):
                count += 1
        return count
    
    def countdepartments(self):
        return len(self.departments)
    
    def mostemployees(self):
        max = 0
        for department in self.departments:
            if len(department.employees) > max:
                max = len(department.employees)
        return department.name, max
            
    def procentageGender(self):
        male = 0
        female = 0
        for department in self.departments:
            for employee in department.employees:
                if employee.gender == "male":
                    male += 1
                elif employee.gender == "female":
                    female += 1
        return male / self.countemployees(), female / self.countemployees()
                    

p1 = Person("Gabriel", "male")
e1 = Employee("David", "male")
dm1 = Departmentmanager("Manuel", "male")
d1 = Department("IT", dm1, [e1, dm1])

e2 = Employee("Masood", "male")
e3 = Employee("Fabian", "male")
dm2 = Departmentmanager("Monika", "female")
d2 = Department("Buchhaltung", dm2, [e2, e3, dm2])

c1 = Company("Touchconnect", [d1, d2])
print(f"number of employees: {c1.countemployees()}")
print(f"number of department managers: {c1.countdepartmentmanager()}")
print(f"number of departments: {c1.countdepartments()}")
print(f"department with most employees: {c1.mostemployees()}")
print(f"procentage of gender: {c1.procentageGender()}")
                
        
