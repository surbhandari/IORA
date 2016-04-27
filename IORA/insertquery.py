#!/usr/bin/python
import psycopg2 as pq
#cn = pq.connect('dbname=mydb user=postgres')
conn = pq.connect("dbname='mydb' user='postgres' host='localhost' password='password'")
print "Opened database successfully"
cur = conn.cursor()
cur.execute("select * from company;")
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (5, 'Paul', 32, 'California', 20000.00 )");
conn.commit()
print "Records created successfully";
conn.close()
