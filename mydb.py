# Serve to create a database but it didn't work

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin12345'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print('All Done!')