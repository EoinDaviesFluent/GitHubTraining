import pyodbc  # We need the module to connecto the db
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()

#CREATE PeopleTable (ID INT, Name VARCHAR(50), Age INT, ALlive BOOL.)

result = cur.execute("CREATE TABLE Student (StudentID INT PRIMARY KEY, FirstName NVARCHAR(50), Surname NVARCHAR(50), Course NVARCHAR(50), City NVARCHAR(50))")

insert_list=["INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (1,'Amber','Aydan','Maths','London')",
             "INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (2,'Caryn','Jeremiah','English','Manchester')",
             "INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (3,'Kevan','Izabelle','Computer Science','Liverpool')",
             "INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (4,'Darren','Britannia','Biology','York')",
             "INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (5,'Jeremy','Elbertson','Engineering','Edinburgh')"]
for insert_query in insert_list:
    result =cur.execute(insert_query)

print ('Generated Table:')
result = cur.execute("SELECT * FROM Student")
for row in result:
    print(row)

result = cur.execute("UPDATE Student SET Course='Cyber Security' WHERE StudentID=3")
print ()
print ('Updated StudentID 3s Course to Cyber Security')
result = cur.execute("SELECT * FROM Student")
for row in result:
    print(row)
user_input=input('Save changes? (t/f): ')
if user_input=='t':
    conn.commit()
    conn.close()
    print ('Saved')
else:
    print ('Not saved')