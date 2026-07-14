class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
class student(person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
    def show_student(self):
        self.display()
        print(f"roll Number : {self.roll_no}")
class teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def show_teacher(self):
        self.display()
        print(f"subject : {self.subject}")
s1 = student("dinesh", 20, 101)
t1 = teacher("kumar", 40, "python")
s1.show_student()
print()
t1.show_teacher()