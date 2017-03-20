# -*- coding: utf-8 -*-
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print [L[0], L[1], L[2]]

r=range(8)
print r
n=3
for i in range(n):
    r.append(L[i])
print r

L = range(5,200,20)
print L
L=range(1,101)
print L[:]
print L[:10]#L[a:b:c]从索引a开始到索引b不含b，没c个取一个
print L[2::3]#取3的倍数
print L[4:50:5]#取<=50且是5的倍数值

print 'ABCDEFG'[:3]
print 'ABCDEFG'[-3:]
print 'ABCDEFG'[::2]
print 'abc'.upper()

#字符串切片操作
def firstCharUpper(s):
    return s[0].upper()+s[1:]
print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')