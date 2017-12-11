#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import requests
import MySQLdb
import socket
import os
from bs4 import BeautifulSoup
import re

singers = []

def loadSinger(conn):
	global singers
	c = conn.cursor()
	sql = "SELECT * FROM singer WHERE active = 1"
	
	try:
		c.execute(sql)
		singers = c.fetchall()
		#get the singers where active = 1
	except MySQLdb.Error,e:
		print e

def getSinger(title,singers,sdata):

	success = 0
	for singer in singers:
		s = re.search(singer[3], title, re.IGNORECASE)
		#compare singer name with raw title
		if s is not None:
			#find singer name in title
			#title = s.group()
			success = 1
			sdata[0] = singer[1]
			sdata[1] = singer[3]
			break
		else:
			pass
	return success

def getYoutubePic(search):
    
    url = "https://www.youtube.com/results?search_query="+search
    requests.packages.urllib3.disable_warnings()

    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,'html.parser')
    link = ""

    for entry in soup.select('a'):
        u = entry.get('href')
        s = re.search(r'/watch?(.*)', u)
        if s is not None:
            #print s.group(1)
            k = s.group(1)
            #print k
            link = k[3:len(k)]
            #print link
            break

    pic_url = "http://i.ytimg.com/vi/"+link+"/0.jpg"
    return pic_url


def getData():
	url = "http://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=17"
	res = requests.get(url, verify=False)
	data = res.json()
	return data

def connectDB():
	try:
		conn = MySQLdb.connect(host="localhost", user="root", passwd="123456qqq", db="data")
		conn.set_character_set('utf8')
		return conn
	except socket.error as serror:
		if conn is not None:
			conn.close()
			
def insertDB(conn,data):

	c = conn.cursor()
	for value in data:
		uid = value["UID"]
		title = value["title"]
		start = value["startDate"]
		end = value["endDate"]
		web = value["webSales"]
		webName = value["sourceWebName"]
		info = value["showInfo"]
		url_pic = getYoutubePic(title)
		
		i = 0
		count = i
		for info_value in info:
			
			time = info_value["time"]
			location = info_value["location"]
			locationName = info_value["locationName"]
			onSales = info_value["onSales"]
			price = info_value["price"]
			lat = info_value["latitude"]
			lon = info_value["longitude"]
			count = count + 1
			
			#process data
			sdata = [0,'']
			process_flag = 0
			if (getSinger(title,singers,sdata)):
				process_flag = 1
			#print sdata[0], sdata[1], process_flag
			
			sql = "INSERT INTO concert(uid,title,singer,singerid,process,start,end,web,webName,count,time,location,locationName,onSales,price,lat,lon,url_pic) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			#print sql
			try:
				c.execute(sql,(uid,title,sdata[1],sdata[0],process_flag,start,end,web,webName,count,time,location,locationName,onSales,price,lat,lon,url_pic) )
				conn.commit()
			except MySQLdb.Error,e:
				print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		#print webName	
		print title
		#print url_pic
	

def closeDB(conn):
	conn.close()
	

conn = None
conn = connectDB()
loadSinger(conn)
data = getData()
insertDB(conn,data)
closeDB(conn)

	
	
	