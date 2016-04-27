#!/usr/bin/python
import psycopg2 as pq
#cn = pq.connect('dbname=mydb user=postgres')
conn = pq.connect("dbname='mydb' user='postgres' host='localhost' password='password'")
print "Opened database successfully"
cur = conn.cursor()
cur.execute("select * from company;")
#cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
rows = cur.fetchall()
for i in rows:
	print "ID = ",i[0]
	print "Name = ",i[1]
	print "Age = ", i[2]
	print "Address = ",i[3]
	print "Salary = ",i[4], "\n"

print "This is all in database"
conn.close()
#f = open('myfile.txt')
#first = f.readline()
#print first

