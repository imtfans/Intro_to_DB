import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying a database)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',      # replace with your MySQL username
        password=''       # replace with your MySQL password
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    # This is required for ALX check
    print("Error while connecting to MySQL:", e)

finally:
    # Safely close cursor and connection
    try:
        cursor.close()
    except NameError:
        pass
    try:
        if connection.is_connected():
            connection.close()
    except NameError:
        pass
