# -*- coding: utf-8 -*-

L=list() #???????????
print L
for x in range(1, 11):
   L.append(x*x) 
print L

L=[x * x for x in range(1, 11)]
print L

print [x*(x+1) for x in range(1,100,2)]
print '\n'

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]
	#isinstance(x, str) 可以判断变量 x 是否是字符串；
	#upper()方法可以返回大写的字母。
print toUppers(['Hello', 'world', 101])

print [ 100*m+10*n+l for m in range(1,10) for n in range(0,10) for l in range(0,10) if m==l]

print [m + n for m in 'ABC' for n in '123']#均为字符串可采用+
