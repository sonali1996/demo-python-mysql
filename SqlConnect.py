import mysql.connector
from mysql.connector
import Error


try: #To connect to the server
connection = mysql.connector.connect(user = 'username',
    host = 'localhost',
    database = 'db_name',
    password = 'Testpass@@123')

if connection.is_connected():
    print("Connected to database")

except Error as e:
    print(Error
        while connecting to mysql, e);
finally
if connection.is_connected():
connecting.close()  #Disconnecting from the server
print("MySQL connection is closed")
