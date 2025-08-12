class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print(f"Name ={self.name} rolllno = {self.rollno} marks = {self.marks}")

s1 = Student("Prabin",21,98)
s1.display()