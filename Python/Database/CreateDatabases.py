import pyodbc  # We need the module to connecto the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)
# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()

#CREATE PeopleTable (ID INT, Name VARCHAR(50), Age INT, ALlive BOOL.)

result = cur.execute("CREATE TABLE PeopleTable (ID INT, Name VARCHAR(50), Age INT, Alive BIT)")
print (result)
result = cur.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'PeopleTable'")
for row in result:
    print(row)
print ()
result =cur.execute("INSERT INTO PeopleTable(ID,Name,Age,Alive) VALUES (1,'Eoin',20,1)")

result = cur.execute("SELECT * FROM PeopleTable")
for row in result:
    print(row)