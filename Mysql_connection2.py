#Connect to a specific database and list its tables

import mysql.connector

# Connect to MySQL with a specific database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@2023",
    database="mysql_db"
)

cursor = conn.cursor()

# Fetch tables from the connected database
cursor.execute("SHOW TABLES")

# Print tables
print("Tables in mysql_db database : ")
for table in cursor:
    print(table[0])

# Close connection
cursor.close()
conn.close()