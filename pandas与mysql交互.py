# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 00:46:52 2021

@author: Mr.P
"""
#从本地读取excel数据
import pandas as pd
import pymysql
path = 'G:\Python_proj\爬取豆瓣TOP250\data'
filename = '豆瓣电影Top250.xls'
data = pd.read_excel(path+'\\'+filename)

#把excel数据写入mysql
con2='mysql+pymysql://root:1111@localhost:3306/scrawl_study?charset=utf8'
data.to_sql('豆瓣电影TOP250',con=con2,if_exists='replace',index=False)  ##导入数据库，如果存在就替换

#从mysql读取excel数据
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1111',
    db = 'scrawl_study'
)
df = pd.read_sql('select * from 豆瓣电影TOP250',conn)