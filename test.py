#!usr/bin/python

name = 'suhua'
pwd = '123'
dbdict={'name':'suhua','pwd':'123'}

if name==dbdict['name'] and pwd==dbdict['pwd']:

    print('name: %s,pwd:%s'%(name,pwd))
else:
    print('name or pwd id error!')
