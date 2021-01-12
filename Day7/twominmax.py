from random import randint
a=[]
for i in range(10):
    v=randint(100,999)
    a.append(v)
a.sort()
print a
print "Max 2:",a[1]
print "Min 2:",a[8]