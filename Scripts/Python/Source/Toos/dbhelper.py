#coding=utf-8
import sqlite3
import os
import sys
import hashlib
import struct

table_name = 'songs'
music_directory = 'D:\OneDrive\Music\MusicNew\7obu'
dictionary = {'.mp3'}

def CalculateMD5Hash(filepath):
	with open(filepath,'rb') as f:
		md5obj = hashlib.md5()
		md5obj.update(f.read())
		hash = md5obj.hexdigest()
		print(hash)
		return hash

conn = sqlite3.connect('contacts.db')
print('''Open database successfully''')

#歌曲表创建语句
create_table_sql = '''CREATE TABLE if not exists ''' + table_name + '''
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL);'''

	   
#歌手表创建语句

conn.execute(create_table_sql)
print("Table created successfully")

current_dir = os.getcwd()
print('current directory:' + current_dir)

#遍历音乐文件夹,三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
for root,dirs,files in os.walk(music_directory):
	#输出文件夹信息
	#for dir in dirs:
	#	print(os.path.join(root,dir))
	for filename in files:
		print("filename is:" + filename)        
		fullfilename = os.path.join(root,filename)
		print("full path:" + fullfilename)
		if filename.lower().endswith('.jpg'): 
			filemd5 = CalculateMD5Hash(fullfilename) 
			print(filemd5)
conn.close()




