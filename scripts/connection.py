#!/usr/bin/python
import psycopg2

try:
    conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='password'")
except:
    print ("I am unable to connect to the database")
