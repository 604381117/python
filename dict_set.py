# -*- coding: utf-8 -*-
dict = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print dict
print dict['Lisa']

if 'Bart' in dict:
    print dict['Bart']
if 'aaaaa' in dict:
    print dict['aaaaa']
	
print dict.get('Adam')
print dict.get('aaaaa') #在Key不存在的时候，返回None

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:',d['Adam']
print 'Lisa:',d['Lisa']
print 'Bart:',d.get('Bart')

d['aaaaa']=100
#d.get('bbbbb')=99  error
d['Adam']=0
print d

for key in d:
    print key + ':', d[key]#遍历
for key in d:
	print key ,':', d[key]
	
s = set(['A', 'B', 'C', 'C'])#set无序
print s
print len(s)

s = set(['Adam', 'adam','bart','Lisa', 'Bart', 'Paul'])
print 'adam' in s
print 'bart' in s

months = set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'
if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'
if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'
	
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0]+":\n",x[1]
	
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for x in L:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print s