# -*- coding: utf-8 -*-
print abs(-12)
print abs(0)
print str(111.0987)
print int(222.0987)
print int('333')
print int("333")
#print int('123.07')  #无法识别
print cmp(-0.34,0)
print cmp(1,1)
print cmp(3,-5)

L = []
x=1
while x<=100:
    L.append(x*x)
    x+=1
print sum(L)

def square_of_sum(L):
    sum=0
    for x in L:
        sum+=x*x
    return sum
        
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

import math #引用头文件，sqrt，sin,cos等
def quadratic_equation(a, b, c):
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2
x,y=quadratic_equation(2, 3, 0)
print "x =",x,',',"y =",y
print quadratic_equation(1, -6, 5)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print fact(5)

def move(n, a, b, c):
    if n==1:
        print a,"-->",c
        return
    move(n-1,a,c,b)
    print a,"-->",c
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

print int('123',8)#8进制

def greet(name='world'):
    print 'Hello,'+name+"."
greet()
greet('Bart')

def power1(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power1(2,10)
	
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(2,5)

def average(*args):
    sum=0.0
    if not len(args):
        return sum
    for x in args:
        sum+=x
    return sum/len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)
