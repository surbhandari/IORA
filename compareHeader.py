#!/usr/bin/python

import psycopg2 as pq
import re
import getpass
#cn = pq.connect('dbname=mydb user=postgres')
#dataBase = raw_input("Enter the database name :")
#usr= raw_input("Enter the User  :")
#host= raw_input("Enter the host :")
#passwd= getpass.getpass('Password :')
 
#conn = pq.connect("dbname="+dataBase+" user="+usr+" host="+host+" password="+passwd)
conn = pq.connect("dbname='mydb' user='postgres' host='localhost' password='password'")
#print "Opened database successfully"
cur = conn.cursor()
print "Connection Established successfully\n"
tableName= raw_input("Enter the Table name :")
#cur.execute("select column_name from information_schema.columns where table_name=\'"+tableName+"\';")
cur.execute("select column_name from information_schema.columns where table_name='company';")
col_name = cur.fetchall()

#print col_name
collist=[]

for item in col_name:
	collist.append(item[0])

#print collist[0]


conn.close()
rawFile= raw_input("Enter the raw file name :")
#f = open('myfile.txt')
try:
	
	f = open(rawFile)
	
except:
	print("There is no such file")
	exit(0)
firstline = f.readline().split('|')
#print firstline

first=[]

for item in firstline:
	#print item
	item = item.strip()
	first.append(item)
	#print item
print "Database : "+ str(collist)
print "Raw file : "+ str(first)
if len(collist)==len(first):
	print "There are same number of column in database and rawfile"
	for items in first:
		if items in collist:
			pass
#			print (str(items) + " found in database")
		else:
			print (str(items) + " not found in database")

else:
	print "There are difference in column number, we need to check"
