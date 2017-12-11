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
######################################
##    Case of Price format          ##   
##    1. 售價: (price)              ##
##    2. 售價: (price)/(num)        ##
##    3. 售價: (price)*(num)        ##
##    4. 售價: (price)(元\塊)       ##
##    5. 售價: (price)(元\塊)/(num) ##
##    6. 售價: (price)(元\塊)*(num) ##
##    7. Other: row of 元           ##
######################################

def refinePrice(price):
        
        result = ''
        
        #pro1: only price
        res = re.search('(\d+)元/張',price)
          
        if res is not None:
           result = res.group(1) 
           #print result.group()
           return result
        else:
            res = re.search('(\d+)元|塊/(\d)張',price)
            if res is not None:
               num     = res.group(2)
               total   = res.group(1)
               return total+'/'+num
        return result

def processPrice(raw):
        success = 0
        price = 0
        seg_list = []
        s = re.search(r'售價(.*)', raw)
        if s is not None:
                success = 1
                #print s.group()
		price = s.group(1)
                #print price + "\n"
                #seg_list=re.findall('[0-9|*|+|,]+',price)
                result = refinePrice(price)
                print result
                
        else:
                #print raw
                pass
       # print seg_list 
       # print  price, "    |||     ".join(seg_list)
        return success

def processTitle(raw,conn,cur,id,singers):

        success = 0
        title = 0
		
        for singer in singers:
           s = re.search(singer[3], raw, re.IGNORECASE)
	   #compare singer name with raw title
		
           if s is not None:
		#find singer name in title
                title = s.group()
                success = 1
                try:
                        sql = "UPDATE ptt SET singer ='"+singer[3]+"' WHERE id = "+ str(id)
                       
                        # print sql
                        cur.execute(sql)
                        conn.commit()
                        sql = "UPDATE ptt SET singerid ="+str(singer[1])+" WHERE id = "+ str(id)
                        # print sql
                        cur.execute(sql)
                        conn.commit()


                except MySQLdb.Error,e:
                        print e
                return success
	   else:
           #s is none 
           #print raw
                pass
        
        return success
		
def getData(conn):
                scount = 0
                count = 0
                cur 	= conn.cursor()
                sql = "SELECT * FROM singer WHERE active = 1"
				
                try:
                    cur.execute(sql)
                    singers = cur.fetchall()
                    #get the singers where active = 1
                except MySQLdb.Error,e:
                    print e
						
	        sql = "SELECT * FROM ptt order by time DESC"
                try:
                        cur.execute(sql)
                        res = cur.fetchall()
                        for record in res:
                               # raw = record[9]
                               # count = count + processPrice(raw)
                                id = record[0]
                                title = record[2]
                                count = count + processTitle(title,conn,cur,id,singers)
                                scount = scount + 1
                except MySQLdb.Error,e:
                        print e
                print "success/total = ", count, "/", scount
				
conn = None
conn = connectDB()
getData(conn)
closeDB(conn)
