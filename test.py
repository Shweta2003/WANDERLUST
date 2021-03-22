import mysql.connector
con=mysql.connector.connect(user="root",host="localhost",password="shweta", database="shweta")
cursor=con.cursor()
a1="CREATE DATABASE STUDENT"
print("student database created successfully")
cursor.execute(a1)
a2="USE STUDENT"
cursor.execute(a2)
print("entered database student successfully")
