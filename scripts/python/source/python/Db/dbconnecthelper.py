#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

class MySQLdbHelper:
    def mysqlConnecter(ip,username,password,dbname):
        db = MySQLdb.connect(ip,username,password,dbname)




