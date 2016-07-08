#coding=utf-8
# help  
# python json_format.py json_text  
import os  
import sys  
import json
import urllib2  
import codecs

outputfile="a.html"  
request = urllib2.Request("http://www.zhihu.com")
response = urllib2.urlopen(request)
print response.read()
filehandle = codecs.open('a.html','w','utf-8')
filehandle.write(str(response.read()))
filehandle.close()


