# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     mysql_test
   Description :
   Author :       a
   date:          2018/9/3
-------------------------------------------------
"""
__author__ = 'a'

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",      # 数据库主机地址
#     user="root",            # 数据库用户名
#     passwd="cGnfs@2018.",   # 数据库密码
#     database="runoob_db"
# )
#
# print(mydb)
#
# mycursor = mydb.cursor()
# mycursor.execute("create database runoob_db")
# mycursor.execute("show databases")
#
# for x in mycursor:
#     print(x)

#mycursor.execute("create table sites (name varchar(255), url varchar(255) )")

def func(a=1,b=1):
    {
        print(a,b)
    }

func(2)