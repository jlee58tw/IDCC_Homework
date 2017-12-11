from django.http import HttpResponse
import MySQLdb
import socket
from django.shortcuts import render

def history(request,pk):
	conn = None
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="bike")
		c = conn.cursor()
		conn.set_character_set('utf8')
		c.execute("SELECT info.sna,info.tot FROM info WHERE sno= "+pk)
		res = c.fetchall()
		
		c.execute("SELECT data.sbi,data.utime FROM data WHERE sno= "+pk+ " AND (MINUTE(utime)%10=0 )ORDER BY utime ASC")
		#c.execute("SELECT data.sbi,data.utime FROM data WHERE sno= "+pk+ " ORDER BY utime ASC")
		res2 = c.fetchall()
		
		conn.close()
	except socket.error as serror:
		if conn is not None:
			conn.close()
	return render(request,"history.html",locals())

def status(request):
	conn = None
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="bike")
		c = conn.cursor()
		conn.set_character_set('utf8')
		c.execute("SELECT data.sno,info.sna,data.tot,data.sbi,data.bemp,data.act,data.utime FROM data JOIN info ON info.sno=data.sno ORDER BY data.utime DESC,data.sno LIMIT 196")
		r = c.fetchall()
		conn.close()
	except socket.error as serror:
		if conn is not None:
			conn.close()
	#return HttpResponse(r)
	return render(request,"status.html",locals())

def show(request):
	conn = None
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="bike")
		c = conn.cursor()
		conn.set_character_set('utf8')
		c.execute("SELECT * FROM info ORDER BY sno")
		r = c.fetchall()
		conn.close()
	except socket.error as serror:
		if conn is not None:
			conn.close()
	#for record in result:
		#print record[0]
	return render(request,"display.html",locals())