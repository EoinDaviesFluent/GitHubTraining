import pyodbc  # We need the module to connecto the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)
# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()




# INSERT 
print ('INSERT:')
#cur.execute("INSERT INTO company(company_no,company_name,tel,county,post_code) VALUES (4500,'Leon Corp','01101 110 001','Gtr Manchester','M1 1AA')")
try:
    cur.execute("INSERT INTO company(company_no,company_name,tel,county,post_code) VALUES (4500,'Leon Corp','01101 110 001','Gtr Manchester','M1 1AA')")
except:
    print ('Unable to Insert - possibly already added')
result = cur.execute("SELECT * FROM company")
#result = cur.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'company'")
for row in result:
    print(row)
print ()


print ('UPDATE:')
#cur.execute("INSERT INTO company(company_no,company_name,tel,county,post_code) VALUES (4500,'Leon Corp','01101 110 001','Gtr Manchester','M1 1AA')")

cur.execute("UPDATE company SET county='West London' WHERE county='London'")


result = cur.execute("SELECT * FROM company")
#result = cur.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'company'")
for row in result:
    print(row)
print ()

print ('DELETE:')
#cur.execute("INSERT INTO company(company_no,company_name,tel,county,post_code) VALUES (4500,'Leon Corp','01101 110 001','Gtr Manchester','M1 1AA')")

#cur.execute("UPDATE company SET county='West London' WHERE county='London'")

#result = cur.execute("DELETE sale WHERE emp_no=50")
result = cur.execute("DELETE salesperson WHERE first_name='Inge'")
result = cur.execute("SELECT * FROM salesperson")
#employee_number_to_delete = cur.execute("SELECT * FROM salesperson WHERE first_name='Janene'")
#print (employee_number_to_delete)
#result = cur.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'sale'")
for row in result:
    print(row)
print ()
#print (len(result))