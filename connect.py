import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            #5 
            try:
                  self.conn = sqlite3.connect('emp.db') #db connection create
                  self.conn.execute('''CREATE TABLE if not exists emp (id INTEGER PRIMARY KEY AUTOINCREMENt,
                                                                  name text , 
                                                                  email text ,
                                                                  mobileno int,
                                                                  type text,
                                                                  exp int,
                                                                  salary int  );''')

            except:      
                  pass
                 
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6
            self.conn.execute("insert into emp values(null,'{}','{}','{}','{}','{}','{}')".format(ename,eemail,emob,etype,eexp,esalary))
            self.conn.commit()

      def display(self):
            #7
            id=int(input("Enter Employee Id : "))
            r=self.conn.execute("select * from emp where id = '{}'".format(id))
            result=(r.fetchall())
            for i in result:
                  print("==================================================")
                  print(i[0])
                  print("Name : "+i[1])
                  print("Email : "+i[2])
                  print("Mobile No. : ",i[3])
                  print("Emp type : "+i[4])
                  print("Experience : ",i[5])
                  print("Salary : " ,i[6])
                  print("==================================================")


            
      
