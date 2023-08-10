import pyodbc  # We need the module to connecto the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)
# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()




# Company 
print ('Company: WHERE count IN (London, Devon)')
result = cur.execute("SELECT * FROM company WHERE county IN ('London','Devon')")
for row in result:
    print(row)
print ()

# Contact
print ('Contact: WHERE company_no BETWEEN 1000 AND 2000')
result = cur.execute("SELECT * FROM contact WHERE company_no BETWEEN 1000 AND 2000")
for row in result:
    print(row)
print ()

# Dept
print ('Dept: WHERE dept_name LIKE %system%')
result = cur.execute("SELECT * FROM dept WHERE dept_name LIKE '%system%'")
for row in result:
    print(row)
print ()

# Sale
print ('Sale: WHERE emp_no=60')
result = cur.execute("SELECT * FROM sale WHERE emp_no=50")
#result = cur.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'sale'")
for row in result:
    print(row)
print ()

# salesperson
print ('Salesperson: WHERE salary<13')
result = cur.execute("SELECT * FROM salesperson WHERE salary<13")
for row in result:
    print(row)
print ()

# We close the connection
conn.close()