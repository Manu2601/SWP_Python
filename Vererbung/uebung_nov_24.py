from enum import Enum

class Gender(Enum):
    MALE = 0
    FEMALE = 1

class Person():
    def __init__(self, name, gender: Gender):
        if name is None:  # Fehler c: neuer Fehler, nicht behebbar
            raise ValueError("A person must have a name")
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
        if departmentmanager is None:  # Fehler a: neuer Fehler, aber behebbar
            print("No department manager assigned, setting to default.")
            departmentmanager = Departmentmanager("Default Manager", Gender.MALE)
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
        department_name = None
        for department in self.departments:
            if len(department.employees) > max:
                max = len(department.employees)
                department_name = department.name
        return department_name, max

    def procentageGender(self):
        male = 0
        female = 0
        for department in self.departments:
            for employee in department.employees:
                if employee.gender == Gender.MALE:
                    male += 1
                elif employee.gender == Gender.FEMALE:
                    female += 1
        try:  # Fehler b: hochgeblubberter Fehler, aber behebbar
            male_percentage = male / self.countemployees()
            female_percentage = female / self.countemployees()
        except ZeroDivisionError:
            male_percentage = 0
            female_percentage = 0
        return male_percentage, female_percentage

# Fehler d: hochgeblubberter Fehler, nicht behebbar
import sys

def my_cli():
    p1 = Person("Gabriel", Gender.MALE)
    e1 = Employee("David", Gender.MALE, "fulltime")

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
    print(f"percentage of gender: {c1.procentageGender()}")

if __name__ == '__main__':
    try:
        my_cli()
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)
