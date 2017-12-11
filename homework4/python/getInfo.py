#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import gzip
import json
import MySQLdb

url = "http://data.taipei/youbike"
print "downloading with urllib"
urllib.urlretrieve(url, "data.gz")
f = gzip.open('data.gz', 'r')
jdata = f.read()
f.close()
data = json.loads(jdata)
conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="bike")
c = conn.cursor()
conn.set_character_set('utf8')


for key,value in data["retVal"].iteritems():
	sno = value["sno"]
	sna = value["sna"]
	tot = value["tot"]
	sbi = value["sbi"]
	sarea = value["sarea"]
	mday = value["mday"]
	lat = value["lat"]
	lng = value["lng"]
	ar = value["ar"]
	sareaen = value["sareaen"]
	snaen = value["snaen"]
	aren = value["aren"]
	bemp = value["bemp"]
	act = value["act"]
	
	sql = "INSERT INTO info(sno,sna,tot,sarea,lat,lng,ar,sareaen,snaen,aren) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	try:
		c.execute(sql,(sno,sna,tot,sarea,lat,lng,ar,sareaen,snaen,aren) )
		conn.commit()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		
	print "NO." + sno + " " + sna

conn.close()
