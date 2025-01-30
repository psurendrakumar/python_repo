#Retrieve data from a specific table using python code

import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@2023",
    database="mysql_db"
)

cursor = conn.cursor()

# Fetch data from a specific table
cursor.execute("SELECT * FROM emp_data")  # Replace with your table name

# Fetch all rows
rows = cursor.fetchall()

# Print each row
print("📊 Table Data:")
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
