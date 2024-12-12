from enum import Enum
class Gender(Enum):
    MALE = 0
    FEMALE = 1

class Person():
    def __init__(self, name, gender: Gender):
        self.name = name
        self.gender = gender
    
class Employee(Person):
    def __init__(self, name, gender: Gender, employmenttype):
        super().__init__(name=name, gender=gender)
        self.employmenttype = employmenttype
        
    def __str__(self):
        return f"{self.name} ({self.gender.value}) is an employee"
    
    def __repr__(self):
        return (f"{type(self).__name__}"
            f'(name="{self.name}", '
            f'gender=Gender.MALE, '
            f'employmenttype="{self.employmenttype}")')
  
        
class Departmentmanager(Employee):
    def __init__(self, name, gender: Gender, employmenttype="fulltime"):
        super().__init__(name=name, gender=gender, employmenttype=employmenttype)
        
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
                if employee.gender == Gender.MALE:
                    male += 1
                elif employee.gender == Gender.FEMALE:
                    female += 1
        return male / self.countemployees(), female / self.countemployees()
                    

p1 = Person("Gabriel", Gender.MALE)
e1 = Employee("David", Gender.MALE, "fulltime")
print(e1)
print(repr(e1))

dm1 = Departmentmanager("Manuel", Gender.MALE)
d1 = Department("IT", dm1, [e1, dm1])

e2 = Employee("Masood", Gender.MALE, "parttime")
e3 = Employee("Fabian", Gender.MALE, "fulltime")
dm2 = Departmentmanager("Monika", Gender.FEMALE)

d2 = Department("Buchhaltung", dm2, [e2, e3, dm2])

c1 = Company("Touchconnect", [d1, d2])
print(f"number of employees: {c1.countemployees()}")
print(f"number of department managers: {c1.countdepartmentmanager()}")
print(f"number of departments: {c1.countdepartments()}")
print(f"department with most employees: {c1.mostemployees()}")
print(f"procentage of gender: {c1.procentageGender()}")

print(dm2.employmenttype)

        
