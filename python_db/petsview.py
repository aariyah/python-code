from get_connection import connect_db


class petsview:

    def connect(self):
        db=connect_db(password="Password@123",database="animal")
        return db

    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="select * from pets"
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    

pv=petsview()
print(pv.get())
        
