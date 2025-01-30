#Establishes a connection to MySQL Workbench and retrieve a list of all databases in MySQL

import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",      # Change if using a remote server
    user="root",           # Your MySQL username
    password="Root@2023"   # Your MySQL password
)

# Check if the connection is successful
if conn.is_connected():
    print("✅Connected to MySQL Server successfully!")

cursor = conn.cursor()

# Execute SQL command to fetch all databases
cursor.execute("SHOW DATABASES")

# Print the databases
print("📂 Databases in MySQL Server:")
for db in cursor:
    print(db[0])

# Close connection
cursor.close()
conn.close()





