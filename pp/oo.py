#!/usr/bin/python
#-*-coding:utf8-*-
# a=9
# def shu():
#     a=0
#     print(a)
# shu()
# print(a)
# a=8
# def kk():
#     a=5
#     print(a)
# kk()
# shu()
# print(a)

# def hanshu(n,j,l):
#     print(n,j,l)
# hanshu('sd',[23,34],('sddsa'))
# hanshu(23,34,45)
# hanshu(56365,456234,234)
# hanshu(34,324,12)

# def maha(a,b,c,d=56,*args,**kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#     print(kwargs)
# maha('ww',23,43,11,2432,'we',4532,mahao='feiwu')





# a=lambda a,b:1 if a==b else 0
# print(a(6,3))

#
# a=['%d*%d=%d'%(j,i,i*j) for i in range(1,10) for j in range(1,i+1) ]
# print(a)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j))
#     print()

# a={123,324,324,12}
# b={4000,9900}
# a.update(b)
# print(a)

# af
# a='wqeewq'
# for i in a:
#     print(i)
# txt=open('ppp.txt',mode='r',encoding='ansi')
# a=txt.read()
# print(a)
# w
# a=True
# if not a :
#     print('错误')
# import random
# a=int(input('请出拳 石头 (1)/ 剪刀 (2)/ 布 (3)'))
# diannao=random.randint(1,3)
# print('玩家选择出拳的是%d 电脑选择出拳的是%d' %(a,diannao))
# if ((a==1 and diannao==2)
#         or (a==2 and diannao==3)
#         or (a==3 and diannao==1)):
#     print('赢了')
# elif a==diannao:
#     print('平了')
# else:
#     print('输了')
# import random
# a=int(input('请输入数字'))
#
# random.randint(1,7)
# i=1
# while i<=5:
#     print('sad')
#     i+=1
# import random
# b = random.randrange(1,4)
# print(b)
# while True:
#     for i in range(3):
#         a = int(input('输入你的选择：石头1/剪刀2/布3'))
#         if a == 1:
#             if b == 1:
#                 print('平局')
#             elif b == 2:
#                 print('赢了')
#             elif b == 3:
#                 print('输了')
#         elif a == 2:
#             if b == 1:
#                 print('输了')
#             elif b == 2:
#                 print('平局')
#             elif b == 3:
#                 print('赢了')
#         elif a == 3:
#             if b == 1:
#                 print('赢了')
#             elif b == 2:
#                 print('输了')
#             elif b == 3:
#                 print('平局')
#     else:
#         break
# try:
#     'jsddsak'
# except TimeoutError as d:
#     print(d)
# else:
#     print('adsdsa')
# import requests
# import re
# a='https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E5%85%A8%E4%B9%A6%E7%BD%91'
# b=requests.get(a)
# c=b.content
# print(c)
# gg=re.compile()
# with open('we.jpg','wb')as a:
#     a.write(c)

# a='asdk3jk\nQaQWDS3443je43'
# b=re.compile('a(.*)3',re.S)
# c=re.findall(b,a)
# c1=b.findall(a)
# print(c1)
# import requests
# import re
# a='http://www.quanshuwang.com/book/9/9055/9674701.html'
# b=requests.get(a)
# c=b.content.decode('gbk')
# q=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
# w=q.findall(c)
# for i in w:
#     print(i.strip('<br />\r\n<br />\r\n'))
# with open('maocai.txt','w',encoding='utf-8')as s:
#     for i in w:
#         s.write(i.strip('<br />\r\n<br />\r\n')+'\n')
# import requests
# import json
# a='https://map.baidu.com/?qt=subwayscity&t=1569031871099'
# d={'User—Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# b=requests.get(a)
# c=b.text
# result=json.loads(c)
# i=0
# while True:
#     try:
# city=result['subways_city']['cities'][1]['cn_name']
# print(city)
# import requests
# import re
# import json
# a='https://movie.douban.com/chart'
# b=requests.get(a)
# c=b.content.decode('utf-8')
# q=re.compile('<a href="https://movie.douban.com/subject/27010768/"  class="">(.*?) / <span style="font-size:13px;">Shanghai Fortress</span>',re.S)
# w=re.findall(q,c)
# with open('ll.txt','w',encoding='utf-8')as a:
#     for i in w:
#         e=a.write(i+'\n')

# import pymysql #用来连接和操作数据库的
# conn=pymysql.connect(host='192.168.2.136',port=3306,user='root',passwd='qwert',db='liang')#charset数据库统一编码  db是数据库名
# #游表
# cusor=conn.cursor()
# # cusor.execute('a')
# cusor.execute('show tables;')
# print(cusor.fetchall())
# cusor.execute('show tables;')
# # print(cusor.fetchall())#获取上一句sql语句的执行结果
# cusor.fetchmany(1)#默认显示结果的第一个
# # cusor.execute('show databases;')
# conn.commit()#提交数据
# conn.close()#断开数据库
# from pp.mh import ss
# ss()
# import pp.mh
# pp.mh.ss()
# import xlwt
# with open('uu.txt','r',encoding='utf-8')as s:
#         b=s.readlines()
#         a=xlwt.Workbook('utf-8')
#         c=a.add_sheet('111')
#         for i,j in enumerate(b):
#
#             c.write(i,0,j)
# a.save('0.xls')
# import requests
# import re
# a='http://www.quanshuwang.com/book/1/1018/326868.html'
# b=requests.get(a)
# c=b.content.decode('gbk')
# v=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*)&gt<script type="text/javascript">style6()',re.S)
# d=re.findall(v,c)
# with open('3.txt','w',encoding='utf-8')as a:
#     for i in d[0]:
#         # print(i)
#         a.write(i.replace('<br />\r\n<br />\r\n&nbsp;&nbsp;&nbsp;&nbsp;','\n'))

# v=[]
# a=[24,34,34,2,21,45]
# a.sort()
# for i in a:
#     if i not in v:
#         v.append(i)
# for j in a:
#     if j==v[-1] or j==v[-2]:
#         print(j)
# with open('ll.txt','r',encoding='utf-8')as a:
#     b=a.readlines()
#     c=(str(b))
#     print(type(c))
#     f=c.strip()
#     print(f)
#
# a=78
# b=89
# c=90
# f=77
# h=(a+b+c+f)/4
# print(h)

def kk(s,*rags):
    a=(s,*rags)
    b=[]
    n=sum(a)/5
    for i in a:
        if i<n:
            b.append(i)
    print(b)
kk(23,43,435,52,231)


