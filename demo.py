import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='ritu',passwd='ritu@12',database='mydatabase')
mycursor=mydb.cursor()
mycursor.execute("select * from patient")
for i in mycursor:
          print(i)
