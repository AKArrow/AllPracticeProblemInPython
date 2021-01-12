from random import randint
a,mx,mx2,mn,mn2=[],0,0,0,0
for i in range(10):
    v=randint(100,999)
    a.append(v)
print a
for i in range(len(a)):
    if a[i]>mx:
        mx=a[i]
for i in range(len(a)):
    if a[i]>mx2 and a[i]!=mx:
        mx2=a[i]
print "Max 2:",mx2
mn=mx
mn2=mx2
for i in range(len(a)):
    if a[i]<mn:
        mn=a[i]
for i in range(len(a)):
    if a[i]<mn2 and a[i]!=mn:
        mn2=a[i]
print "Min 2:",mn2