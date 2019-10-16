#!/usr/bin/python
#-*-coding:utf8-*-


# for j in enumerate(10):
#     print(j)
# import xlwt
# c = xlwt.Workbook('utf-8')
# r = c.add_sheet('iii')
#
# r.write(r.xls)
# for i in range(1,100,2):
#     print(i)
#发送邮件 smtplib
# import smtplib #封装了smtp协议
# import email.mime.text#处理正文中的数据的
# import email.mime.multipart#封装的邮件的格式
# sender='l13723282692@163.com'
# reser=['2353348445@qq.com','mc1832713135@163.com','13781147317@163.com','15039008093@163.com']
# server='smtp.163.com'
# passwd='qwert123'#授权码
# message=email.mime.multipart.MIMEMultipart()#创建一个空邮箱
# message['From']=sender#发件人
# message['TO']=''.join(reser)#收件人
# message['Subject']='python_learn'#主题
# a="""马浩是个帅哥
# """
# cc=email.mime.text.MIMEText(a)
# message.attach(cc)#将正文添加到邮件里
# att1=email.mime.text.MIMEText(open('D:\\图片\\SPJZWJGNO)B9AS`%0UN`Z%0.png','rb').read(),'base64','utf-8')#定义发送的附件的文件名，文件可以是任何格式
# att1["Content-type"]='application/octet-stream'
# att1["Content-Disposition"]='attachment;filename="test.png"'
# message.attach(att1)#将附件发送到邮箱里
# att2=email.mime.text.MIMEText(open('mh.py','rb').read(),'base64','utf-8')#定义发送的附件的文件名，文件可以是任何格式
# att2["Content-type"]='application/octet-stream'
# att2["Content-Disposition"]='attachment;filename="test.txt"'
# message.attach(att2)#将附件发送到邮箱里
# smtp123=smtplib.SMTP_SSL(server,465)#定义发送邮件的服务器和端口号
# smtp123.login(sender,passwd)#登录服务器
# smtp123.sendmail(sender,reser,message.as_string())#发送邮件
# smtp123.close()#断开连接
# for i in range(10):
#     for j in range(1,i+1):
#      print('{}*{}={}'.format(i,j,i*j),end=' ')
#     print('')
# a=[]
# for i in range(2,100):
#     for j in range(2,i):
#         if (i%j==0):
#             break
#     else:
#         a.append(i)
#
#         print(a)
# a=int(input('请输入边长'))
# b=int(input('请输入边长'))
# c=int(input('请输入边长'))
# if a+b>c:
#     if a**2+b**2>c**2:
#         print('是锐角三角形')
#     elif a**2+b**2<c**2:
#         print('钝角三角形')
#     elif a**2+b**2==c**2:
#         print('直角三角形')
#
# import xlwt
# b=xlwt.Workbook('utf-8')
# c=b.add_sheet('111')
# c.write(0,0,123)
# b.save('1.xls')
# import random
# a=0
# c=int(input('ss'))
# for i in range(1,c+1):
#     if c%i==0:
#         a+=i
# print(a)
# a=[]
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a.append(i)
#         print(min(a))
# print(sum(range(1,21)))
# def age(x):
#     if x>1:
#         return 2+age(x-1)
#     else:
#         return
# age(2)
# def tm028():
#     print(age(5))
#
# a='sad dsa dsa 23234 43521 '
# a=[]
# for i in range(101,200):
#     for j in range(101,i):
#         if i%j==0:
#             break
#     else:
#         a.append(i)
#         print(sum(a))
# a='1231432432323'
# print(a[2:3])
# a={'jj':'32','jjhk':'ggga','vhgsad':'dcvfa'}
# a['32']='jj'
# print(a)
# a=hex(999)
# print(a)
# import xlwt
# # g=[1,2,3,4,5,6,7,8,9,10]
# c=xlwt.Workbook('utf-8')
# b=c.add_sheet('111')
# for i in range(0,10):
#     for j in range(0,10):
#         b.write(i,j,'123')
# c.save('i.xls')
# import pymysql
# a=pymysql.connect('192.168.2.12',3306,'root','qwert')
# b=a.cursor()
# b.execute('use liang')
# with open('d.xls','r',encoding='utf-8')as f:
#     b=f.readlines()
# a=0
# b=0
# while a<=100:
#     b=b+a
#     a=a+1
# print(b)
# a=2
# b=2
# s = []
# while a<=100:
#     a+=1
#     while b<=a:
#       if a%b==0:
#           break
#       else:
#         s.append(a)

