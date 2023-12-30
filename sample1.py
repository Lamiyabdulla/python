class personal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
class qualification:
    def __init__(self,degree_name,total_marks,percentage):
        self.degree_name=degree_name
        self.total_marks=total_marks
        self.percentage=percentage
    def get(self):
        print("degree:",self.degree_name)
        print("total marks:",self.total_marks)
        print("percentage:",self.percentage)
obj_personal=personal("lamiya",22)
obj_qualification=qualification("bsc.phy",500,70.0)
obj_personal.display()
obj_qualification.get()
