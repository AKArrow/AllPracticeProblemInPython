from random import randint
a,b,c,d,e=randint(100,999),randint(100,999),randint(100,999),randint(100,999),randint(100,999)
print a,b,c,d,e
if a>b and a>c and a>d and a>e:
    print a,"Is Maximum"
elif b>a and b>c and b>d and b>e:
    print b,"Is Maximum"
elif c>a and c>b and c>d and c>e:
    print c,"Is Maximum"
elif d>a and d>b and d>c and d>e:
    print d,"Is Maximum"
elif e>a and e>b and e>c and e>d:
    print e,"Is Maximum"
if a<b and a<c and a<d and a<e:
    print a,"Is Minimum"
elif b<a and b<c and b<d and b<e:
    print b,"Is Minimum"
elif c<a and c<b and c<d and c<e:
    print c,"Is Minimum"
elif d<a and d<b and d<c and d<e:
    print d,"Is Minimum"
elif e<a and e<b and e<c and e<d:
    print e,"Is Minimum"