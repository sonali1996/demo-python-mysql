import mysql.connector
 
 
# To connect to the server
connection = mysql.connector.connect(user = 'username',
                               host = 'localhost',      
                              database = 'db_name',
                               password = 'Testpass@@123')
 
print(connection)
 
# Disconnecting from the server
connecting.close()
