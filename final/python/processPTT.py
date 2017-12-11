# -*- coding: utf-8 -*-
import requests
import urllib2
import re
from bs4 import BeautifulSoup
import MySQLdb
import socket
import datetime


def connectDB():
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="123456qqq", db="data")
		conn.set_character_set('utf8')
		return conn
	except socket.error as serror:
		if conn is not None:
			conn.close()

def closeDB(conn):
	conn.close()
	
def processPrice(raw):
	
	success = 0
	price = 0
	seg_list = []

	s = re.search(r'售價(.*)', raw)
	if s is not None:
		price = s.group(1)
		seg_list=re.findall('[0-9|*|+|,]+',price)
		success = 1
	else:
		#print raw
		pass
	print  price, "/ ".join(seg_list)
	return success
	
def processTitle(raw,conn,c,id):
	
	success = 0
	title = 0

	s = re.search('張清芳', raw)
	if s is not None:
		title = s.group()
		success = 1
		try:
			sql = "UPDATE ptt SET concert = 13 WHERE id = "+ str(id);
			#print sql
			#c.execute(sql)
			#conn.commit()
		except MySQLdb.Error,e:
			print e
		
	else:
		#print raw
		pass
	print  title, raw
	return success
	
def getData(conn):
		
		scount = 0
		count = 0
		
		c = conn.cursor()
		sql = "SELECT * FROM ptt order by time DESC"
		try:
			c.execute(sql)
			res = c.fetchall()
			for record in res:
				#raw = record[9]
				#count = count + processPrice(raw)
				id = record[0]
				title = record[2]
				count = count + processTitle(title,conn,c,id)
				scount = scount + 1

		except MySQLdb.Error,e:
			print e

		print "success/total = ", count, "/", scount
		
conn = None
conn = connectDB()
getData(conn)
closeDB(conn)
