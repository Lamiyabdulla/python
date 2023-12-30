class personal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
class qualification:
    def __init__(self,degree_name,total_marks,percentage):
        self.dname=degree_name
        self.marks=total_marks
        self.percentage=percentage
    def display(self):
        print("degree:",self.dname)
        print("total marks:",self.marks)
        print("percentage:",self.percentage)
    def eligible(self):
        if self.percentage>=60 and self.marks>=500:
            print("the student is eligible for mca")
        else:
            print("the student is not eligible for mca")
obj_personal=personal("lamiya",22)
obj_qualification=qualification("bca",450,59.0)
obj_personal.display()
obj_qualification.display()
obj_qualification.eligible()
