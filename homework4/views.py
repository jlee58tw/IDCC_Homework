from django.http import HttpResponse
import MySQLdb
import socket
def show(request):

	conn = None
	
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="bike")
		c = conn.cursor()
		conn.set_character_set('utf8')
		c.execute("SELECT * FROM info")
		result = cursor.fetchall()
		conn.close()
	except socket.error as serror:
		if conn is not None:
			conn.close()
	#for record in result:
		#print record[0]
	return HttpResponse(result)