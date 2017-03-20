# -*- coding: utf-8 -*-
age = 20
if age >= 18: #冒号不能丢
    print 'your age is', age
    print 'adult'
else:
    print "your age is",age
	#print "aaaaa" if最后一个语句块只能为一条语句？
print 'END'

if age >= 18:
    print 'adult'
else:
    if age >= 6:
        print 'teenager'
    else:
        if age >= 3:
            print 'kid'
        else:
            print 'baby'

if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'
	
score = 85
if score>=90:
    print 'excellent'
elif score>=80:
    print 'good'
    print "aaaaa"
elif score>=60:
    print 'passed'
else:
    print 'failed'
	
L = [75, 92, 59, 68]
sum = 0.0
for a in L:
    sum+=a
	# print sum+=a  替换上一行不通过为何？只能有一条语句？
print sum / 4

N = 10
x = 0
while x < N:
    print x
    x = x + 1
	
sum = 0
x = 1
n = 1
while True:
    if n>20:
        break
    sum  = sum + x
    n+=1
    x = x*2
print sum

sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print sum

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print x * 10 + y
