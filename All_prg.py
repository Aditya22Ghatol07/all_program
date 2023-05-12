import sys


l1=[1,2,3,4,5,6,12,13,46,79,100,20,50,60,15000]
n=len(l1)
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]<l1[j]:

            l1[i],l1[j]=l1[j],l1[i]
            print(l1[1])



1111111111111111111111111111111111111111111111111111111111111




sys.exit(0)
l1 = [1, 2, 2, 2, 1, 1, 1, 1, 13, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 6, 20, 25, 90]
n = len(l1)
for i in range(0, n):
    for j in range(i + 1, n):
        if l1[i] == l1[j]:
            print(l1[i], end='')

sys.exit(0)
s1='pune'
s2=''
i=len(s1)-1
while i>=0:
    s2=s2+s1[i]
    i=i-1
    print(s2,end=' ')


sys.exit(0)
##########################################################
s1='pune is great city'
l=s1.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1

print(l1)
out=' '.join(l1)
print(out)
sys.exit(0)


s1='pune is greate city'
l=s1.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
    print(l1)
    out=' '.join(l1)
    print(out)
    print()
    print()




sys.exit(0)
s1='pune is great city'
l=s1.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1

print(l1)
out=' '.join(l1)
print(out)



sys.exit(0)

s1='123456789'
#i=0
i=0
while i<len(s1):
    print(s1[i],end=' ')
    i=i+2


s1='ponijkhjhkhghkbbbkb'
print(len(s1))

s='pune'
#i=0
i=1
while i<len(s):
    print(s[i],end=' ')
    i=i+2



s1='pune'
print(s1[::2])


l1=[]
l2=[]
for j in range(20):
    if j%2==0:
        l1.append(j)
        print(l1)
    else:
        l2.append(j)
        print(l2)
l1=[]
l2=[]
for j in range(10):
    if j%2==0:
        l1.append(j)
        print(l1,'even')
    else:
        l2.append(j)
        print(l2,'odd')

l1=[1,2,3,4,5,6,7,8,9]
l2=[2,4,6,8,1]
l3=[]
for i in l1:
    if i  in l2:
        l3.append(i)
        print(l3)




l1=[1,2,3,4,5,6,7,8,9]
l2=[2,4,6,8]
l3=[i*i*i for i in l1 if i not in l2]
print(l3)


l1=[1,2,3,4,5,6,7,8,9]
l2=[2,4,5,6,8]
l3=[i*i for i in l1 if i not in l2]
print(l3)


#s1='dgdgdgdgdgddgdggggggggggggggg'
#print(s1[::-1])
s1='pune is great city if ewfhhhgfeeeeghgjgjggggjggtttttteeeeee'
input1='e,a,i,o,u,g'
for ch in s1:
    if ch=='g':
        print('hi')
    else:
        print(ch)


a='aditya'
b='ghatol'
print(a+' '+b)




s1='pune is great city if we want to do any thing'
input='a,e,i,o,u'
for ch in s1:
    if ch=='e':
        print('hi',end=' ')
    else:
        print(ch,end='')




s='dgfgfgfr65655ffy657fyf'
s1=''
s2=''
for i in s:
    if i.isalpha():
        s1=s1+i
        print(s1)
    else:
        s2=s2+i
        print(s2)

a='adgdgdgdgf5665gffgfgdf'
a1=''
a2=''
for i in a:
    if i.isalpha():
        a1=a1+i
    else:
        a2=a2+i
        print(a2)
ab='ssssssssssssssssssssssssssddgfhfhfhghgfhytedy'
print(ab.count('s'))
an='dfhgghgggg'
print(an.isdigit())

c=['aditya','ghatol']
l1='_'.join(c)
print(l1)

q='aditya ghatol'
at=q.split('a')
print(at)

r='aditya ghatol'
t=r.split('l')
print(t)

y='aditya ghatol'
b=list(reversed(y))

print(''.join(b))


u='aditya ghatol'
a=list(reversed(u))
print(''.join(a))
