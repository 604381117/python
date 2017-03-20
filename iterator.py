# -*- coding: utf-8 -*-
for i in range(1,100):
    if i%7==0:
        print i
		
L = ['Adam', 'Lisa', 'Bart', 'Paul']
r=range(1,5)
z=zip(r,L)
for index, name in z:
    print index, '-', name
	

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name

t=tuple()
print t
for t in enumerate(L):
    idx = t[0]
	nam = t[1]
    print idx, '-', nam      #?????????????
	
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
for v in d.values():#生成values的list占用内存空间
    print v
print d.itervalues()#直接从dict中取值
for v in d.itervalues():
    print v

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
print d.items()
sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k,':',v
	
print 'average', ':', sum/len(d)