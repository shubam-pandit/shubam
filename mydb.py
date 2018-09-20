import sqlite3
from sqlite3 import Error
try:
    connection = sqlite3.connect("C:\\Users\Linux Lab\Documents\database.db")
except Error as e:
    print(e)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS telecom (
   SNo INT,
   PlanName VARCHAR(20),
   MonthlyRental INT,
   FreeInternet INT,
   FreeCalls INT,
   FreeSms INT,
   CallCharges INT,
   DataCharges INT,
   PRIMARY KEY (SNo))'''
);
#Putting the information about the plans into the table
cursor.execute("INSERT INTO 'telecom'(SNo,PlanName,MonthlyRental,FreeInternet,FreeCalls,FreeSms,CallCharges,DataCharges) VALUES(1,'A',400,0,0,0,200,200)");
cursor.execute("INSERT INTO 'telecom'(SNo,PlanName,MonthlyRental,FreeInternet,FreeCalls,FreeSms,CallCharges,DataCharges) VALUES(2,'B',800,1,0,1,400,200)");
cursor.execute("INSERT INTO 'telecom'(SNo,PlanName,MonthlyRental,FreeInternet,FreeCalls,FreeSms,CallCharges,DataCharges) VALUES(3,'C',500,1,0,1,200,200)");
cursor.execute("INSERT INTO 'telecom'(SNo,PlanName,MonthlyRental,FreeInternet,FreeCalls,FreeSms,CallCharges,DataCharges) VALUES(4,'D',800,1,0,1,200,200)");
cursor.execute("INSERT INTO 'telecom'(SNo,PlanName,MonthlyRental,FreeInternet,FreeCalls,FreeSms,CallCharges,DataCharges) VALUES(5,'E',700,1,1,0,200,200)");
cursor.execute("INSERT INTO 'telecom'(SNo,PlanName,MonthlyRental,FreeInternet,FreeCalls,FreeSms,CallCharges,DataCharges) VALUES(6,'F',1000,0,1,1,200,200)");
#Save the changes
connection.commit()

print("The various plan details are")
print("The enteries are in the order PlanSerialno,PlanName,MonthlyRental,FreeInternet,FreeCalls,FreeSms,Callcharges,Datacharges")
#To list the details of all the  plans from the database
cursor.execute("SELECT * FROM telecom")
results = cursor.fetchall()
for r in results:
    print(r)

    
cursor.close()
connection.close()
