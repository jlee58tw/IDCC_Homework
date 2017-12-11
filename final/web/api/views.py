from django.http import JsonResponse
import json
import itertools
import MySQLdb
from django.contrib.auth.decorators import login_required  
from datetime import datetime

def connectDB():
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="123456qqq", db="data")
		conn.set_character_set('utf8')
		return conn
	except socket.error as serror:
		if conn is not None:
			conn.close()


def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(itertools.izip([col[0] for col in desc], row)) 
            for row in cursor.fetchall()]

def closeDB(conn):
	conn.close()

def getConcert(request):

	if request.method == 'GET':
		#id = request.GET['id']
		conn = None
		conn = connectDB()
		c = conn.cursor()
		sql = "SELECT * FROM concert where count=1"
		try:
			c.execute(sql)
			res = dictfetchall(c)
			conn.commit()
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})
		closeDB(conn)

		return JsonResponse({	"success" : "true", "data" : res})
	else:
		return JsonResponse({"success" : "false","error" : "method"})

def getPTT(request):

	if request.method == 'GET':
	
		page = request.GET['page']
		start = (int(page) - 1) * 20
		conn = None
		conn = connectDB()
		c = conn.cursor()
		sql = "SELECT * FROM ptt order by time DESC limit "+str(start)+",20"
		try:
			#pass
			c.execute(sql)
			res = dictfetchall(c)
			conn.commit()
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})

		sql = "SELECT * FROM ptt"
		try:
			c.execute(sql)
			count = c.rowcount
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})
		
		if request.user.is_authenticated():
			user = request.user
			sql = "SELECT singerid FROM subscribe where userid = "+str(user.id)
			try:
				c.execute(sql)
				subsinger = dictfetchall(c)
				conn.commit()
			except MySQLdb.Error,e:
				return JsonResponse({"success" : "false","error" : "db"})
		else:
			subsinger = ""
			
		closeDB(conn)

		return JsonResponse({	"success" : "true", "data" : res, "page" : page, "count" : count, "subsinger": subsinger})
	else:
		return JsonResponse({"success" : "false","error" : "method"})

def getPTTnum(request):

	if request.method == 'GET':
		conn = None
		conn = connectDB()
		c = conn.cursor()
		sql = "SELECT * FROM ptt"
		try:
			c.execute(sql)
			res = c.rowcount
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})
		closeDB(conn)

		return JsonResponse({"success" : "true", "num" : res})
	else:
		return JsonResponse({"success" : "false","error" : "method"})

@login_required
def addSubscribe(request):

	if request.method == 'GET':
		user = request.user
		singerid = request.GET['singerid']
		
		conn = None
		conn = connectDB()
		c = conn.cursor()
		
		sql = "SELECT name FROM singer where id = "+str(singerid)
		try:
			c.execute(sql)
			singername = c.fetchone()
			conn.commit()
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : singername})
		
		sql = "SELECT * FROM subscribe where userid = "+str(user.id)+" and singerid = " + str(singerid)
		try:
			c.execute(sql)
			count = c.rowcount
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})
		
		if count > 0:
			return JsonResponse({"success" : "false","error" : "already add"})
		
		sql = "INSERT INTO subscribe(userid,singerid,singername,email,time) VALUES(%s,%s,%s,%s,%s)"
		try:
			c.execute(sql,(user.id,singerid,singername,user.email,datetime.now()))
			conn.commit()
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})
		closeDB(conn)

		return JsonResponse({ "success" : "true", "singerid" : singerid})
	else:
		return JsonResponse({"success" : "false","error" : "method"})
		
@login_required
def getSubscribe(request):

	if request.method == 'GET':
		user = request.user
		
		conn = None
		conn = connectDB()
		c = conn.cursor()
		
		sql = "SELECT singerid,singername,time FROM subscribe where userid = "+str(user.id)
		try:
			c.execute(sql)
			res = dictfetchall(c)
			conn.commit()
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})

		closeDB(conn)

		return JsonResponse({ "success" : "true", "data" : res})
	else:
		return JsonResponse({"success" : "false","error" : "method"})
		
@login_required
def delSubscribe(request,id):

	if request.method == 'DELETE':
		user = request.user
		conn = None
		conn = connectDB()
		c = conn.cursor()
		
		sql = "DELETE FROM subscribe where userid = "+str(user.id)+" and singerid = "+str(id)
		try:
			c.execute(sql)
			conn.commit()
		except MySQLdb.Error,e:
			return JsonResponse({"success" : "false","error" : "db"})

		closeDB(conn)

		return JsonResponse({ "success" : "true", "singerid" : id})
	else:
		return JsonResponse({"success" : "false","error" : "method"})
