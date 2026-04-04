# hybrid and heirarchial inheritance in python

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


# Hierarchical inheritance (Person → Student, Teacher)
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show_student(self):
        print(f"Roll No: {self.roll}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_teacher(self):
        print(f"Subject: {self.subject}")


# Hybrid inheritance (multiple inheritance)
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, roll, subject, stipend):
        Student.__init__(self, name, roll)
        Teacher.__init__(self, name, subject)
        self.stipend = stipend

    def show_ta(self):
        print(f"Stipend: {self.stipend}")


# ---- Usage ----

print("=== Student ===")
s = Student("Alex", 101)
s.show_name()
s.show_student()

print("\n=== Teacher ===")
t = Teacher("John", "Physics")
t.show_name()
t.show_teacher()

print("\n=== Teaching Assistant (Hybrid) ===")
ta = TeachingAssistant("Emma", 202, "Math", 5000)
ta.show_name()
ta.show_student()
ta.show_teacher()
ta.show_ta()
