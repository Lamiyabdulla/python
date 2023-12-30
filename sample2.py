class personal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
class qualification:
    def __init__(self,degree_name,total_mark,percentage):
        self.dname=degree_name
        self.marks=total_mark
        self.percentage=percentage
    def display(self):
        print("degree:",self.dname)
        print("total marks:",self.marks)
        print("percentage:",self.percentage)
obj_person=personal("lami",22)
obj_qualification=qualification("bsc.phy",500,70.0)
obj_person.display()
obj_qualification.display()
