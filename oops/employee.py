class Employee:

    id:int
    name:str
    desig:str
    salary:int

    def __init__(self,id,name,desig,salary) -> None:


    
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary


    def get_emp(self):
        print(self.name,self.id,self.desig,self.salary)


emp1=Employee()

emp1.set_emp(100,"hari","hr",38000)
emp1.get_emp()


