from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from models import Ptt,Concert,Subscribe
import MySQLdb

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

def index(request):
	return render(request,"web/index.html",locals())

def ticket(request):
	user = request.user
	return render(request,"web/ticket.html",locals())
	
def ticket2(request,id):
	
	page = 1
	user_flag = 0
	sub_flag = 0

	if request.method == 'GET':
	
		if 'page' in request.GET:
			page = request.GET['page']
			
		if id == '0':
			posts = Ptt.objects.all().order_by('-time')
		else:
			id = str(id)
			posts = Ptt.objects.filter(singerid=id).order_by('-time')
			
		concerts = Concert.objects.filter(count='1',process='1')
		
		subscribes = []
		if request.user.is_authenticated():
			user = request.user
			user_flag = 1
			subscribes = Subscribe.objects.filter(userid=user.id)
		if len(subscribes) > 0 :
			sub_flag = 1

		return render(request,"web/ticket2.html",locals())
	
def concert(request):
	return render(request,"web/concert.html",locals())
	
def item(request):
	return render(request,"web/item.html",locals())
	
def detail(request,id):

	if request.method == 'GET':
		id = str(id)
		concert = Concert.objects.filter(id=id)
	
		return render(request,"web/detail.html",locals())

@login_required
def subscribe(request):
	user = request.user
	return render(request,"web/subscribe.html",locals())