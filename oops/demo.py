class Student:

    rollno:int
    name:str
    course:str

    def __init__(self,roll,name,course) -> None:
        
    

    
        self.rollno=roll
        self.name=name
        self.course=course


    def get_student(self):
        print(self.rollno,self.name,self.course)


obj=Student(1000,"hari","django")
obj.get_student()