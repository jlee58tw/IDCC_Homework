import re
import requests
from bs4 import BeautifulSoup
import MySQLdb
import datetime

def connectDB():
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="ppp", db="ticket")
		conn.set_character_set('utf8')
		return conn
	except socket.error as serror:
		if conn is not None:
			conn.close()

def closeDB(conn):
	conn.close()
	
def insertDB(conn,title,pid,ptime,author,raw,url):

	c = conn.cursor()
	gtime = datetime.datetime.now()
	print title,pid,ptime,author,raw,url
	
	#sql = "INSERT INTO ptt(postid,title,author,time,process,concert,price,num,raw,url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	#print sql
	#try:
	#	c.execute(sql,(postid,title,author,time,process,concert,price,num,raw,url) )
	#	conn.commit()
	#except MySQLdb.Error,e:
	#	print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getContent(url,pid,title,conn):

	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept':'text/html;q=0.9,*/*;q=0.8','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding':'gzip','Connection':'close'}
	res = requests.get(url, verify=False, headers=headers)
	soup = BeautifulSoup(res.text,'html.parser')
	
	raw = soup.find('td', id=re.compile("postmessage_\d+")).text
	ptime = soup.find('em', id=re.compile("authorposton\d+")).text
	author = soup.find('a', class_="author-id").text
	insertDB(conn,title,pid,ptime,author,raw,url)


def getPage(conn):
	
	url = 'http://www.citytalk.tw/bbs/forum.php?mod=forumdisplay&fid=107'
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept':'text/html;q=0.9,*/*;q=0.8','Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding':'gzip','Connection':'close'}
	res = requests.get(url, verify=False, headers=headers)
	soup = BeautifulSoup(res.text,'html.parser')
	a = soup.findAll("a", class_="s")
	#print res.request.headers
	
	c = 4
	for link in a:
		surl = link.get('href')
		c = c - 1
		if c < 0:
			break
		if not re.search(r'thread-51', surl) and not re.search(r'thread-160193', surl) and not re.search(r'thread-50261', surl):
			print surl
			d = re.match(r'thread-(\d+)-(.*)',surl)
			pid = d.group(1)
			title = d.group(2)
			print pid, title
			#getContent('http://www.citytalk.tw/bbs/'+surl,pid,title,conn)
 
conn = None
conn = connectDB()

getPage(conn)

closeDB(conn)
