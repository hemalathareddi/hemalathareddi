class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40
s1 = Student("Ravi", 85)
s2 = Student("Sita", 30)
if s1.is_passed():
    print(s1.name, "Passed")
else:
    print(s1.name, "Failed")
if s2.is_passed():
    print(s2.name, "Passed")
else:
    print(s2.name, "Failed")


class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    def display(self):
        print(self.name, "works at", Employee.company_name)
e1 = Employee("Arjun")
e2 = Employee("Meena")
e1.display()
e2.display()
Employee.change_company("Infosys")  # change for all
print("\nAfter Change:")
e1.display()
e2.display()

class MathOps:
    @staticmethod
    def is_even(num):
        return num % 2 == 0
print("10 is Even:", MathOps.is_even(10))
m = MathOps()
print("7 is Even:", m.is_even(7))


class Car:
    wheels = 4

    def __init__(self, mileage):
        self.mileage = mileage

    def display_specs(self):
        print("Mileage:", self.mileage, "Wheels:", Car.wheels)

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels
c1 = Car(18)
c1.display_specs()
Car.change_wheels(6)
print("After Change:")
c1.display_specs()


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def show_conversion(self):
        f = Temperature.to_fahrenheit(self.celsius)
        print(f"{self.celsius}°C = {f}°F")
t1 = Temperature(25)
t1.show_conversion()


class Course:
    total_students = 0  # class variable

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students += 1
        print(self.student_name, "enrolled")

    @classmethod
    def show_total(cls):
        print("Total Students:", cls.total_students)

    @staticmethod
    def is_eligible(age):
        return age >= 18
s1 = Course("Ravi")
s2 = Course("Sita")
s3 = Course("Arjun")
s1.enroll()
s2.enroll()
s3.enroll()
Course.show_total()
print("Age 20 Eligible?", Course.is_eligible(20))


class BankAccount:
    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"{amount} deposited. New Balance: {self.balance}")
        else:
            print("Invalid Amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def display(self):
        print(f"{self.holder} - Balance: {self.balance} - Bank: {BankAccount.bank_name}")
acc1 = BankAccount("Ravi", 5000)
acc1.display()
acc1.deposit(2000)
acc1.deposit(-500)
BankAccount.change_bank_name("HDFC")
print("\nAfter Bank Name Change:")
acc1.display()



