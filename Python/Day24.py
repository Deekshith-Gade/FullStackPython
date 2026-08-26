class Student:
    collegename="codegnan"
    def __init__(self):
        self.name='raju'
        self.age=24
        # print("My college name is",Student.collegename)
        # Student.collegename="jntu"
        # print("My college name is",Student.collegename)
    #Instance Method
    def Talk(self):
        print("My name is",self.name)
        print("My age is ",self.age)
      
    @classmethod
    def show(cls):
        print("My college name is",cls.collegename)
        print("My college name is",cls.collegename)
        cls.collegename="jntu"
        print("My college name is",cls.collegename)
    @staticmethod
    def Display():
        print("Iam from static method")
s1=Student()
s1.Talk()
Student.show()
Student.Display()


class employee:
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
    def Display(self):
        print("My name is",self.name)
        print("My empid",self.empid)
s1=employee("raju","1")
s1.Display()
print()
s2=employee("Harish","2")
s2.Display()
