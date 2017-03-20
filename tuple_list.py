# -*- coding: utf-8 -*-
print 'Hello,world.'
print "Hello,world."
a=True
print a and 'a=T' or 'a=F'
print a and 'a=T' and 'a=F'

a = 'python'
print 'hello,',a or 'world'   #逗号不能去除
b = ''
print 'hello,',b or 'world'

L = ['Adam', 95.5,'Lisa', 85, 'Bart', 59]
print L
print L[-1]
print L[-2]
print L[-3]
print L[-4]
print L[-5]
print L[-6]
L = ["Adam", 95.5, "Lisa", 85, "Bart", 59]
print L

print L[0]
print L[1]
print L[2]
print L[3]
print L[4]
print L[5]
L.insert(4,'insert')  #不能为双引号
L.append('append')  
print L
print L.pop()
print L
print L.pop(0)
print L
#  a=85
#  L.pop(a)  错误的用法
a=L[0]
L[0]=L[-1]
L[-1]=a
print L

t = ('aaa',34,45,67,23.45,-345,"234sdfsdg",'  ',"True")
print t
t=(1)
print t
t=(1,)
print t
t=("aaaaa")
print t
t=("aaaaa",)
print t


t = ('a', 'b', ['A', 'B']) #tuple内部元素各个元素的指向永远不变
print t
L=t[2]
L[0]="aa"
L[1]='bb'
print t

t = ('a', 'b', ('A', 'B')) #tuple内部元素各个元素的指向永远不变
print t
L=t[2]
#L[0]='a'
#L[1]='b'  运行不过，不可改变
print t





