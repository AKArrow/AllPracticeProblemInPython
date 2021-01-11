d=input("Enter A Day:")
m=raw_input("Enter A Month:")
if m=='march' and d>=20 and d<=31:
    print "True"
elif m=='april' and d>=1 and d<=30:
    print "True"
elif m=='may' and d>=1 and d<=31:
    print "True"
elif m=='june' and d>=1 and d<=20:
    print "True"
else:
    print "False"