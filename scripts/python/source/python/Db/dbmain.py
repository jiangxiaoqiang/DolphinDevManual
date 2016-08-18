#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import dbconnecthelper

def main(argv):
    dbconnecthelper.MySQLdbHelper.mysqlConnecter("120.26.132.144","root","123456789","mvsp")

if __name__ == "__main__":
    main(sys.argv)
