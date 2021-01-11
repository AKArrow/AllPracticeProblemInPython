a,b,c=input("Enter 1st Number"),input("Enter 2nd Number"),input("Enter 3rd Number")
op1,op2,op3,op4=a+b*c,a%b+c,c+a/b,a*b+c
print "Opration 1:",op1
print "Opration 2:",op2
print "Opration 3:",op3
print "Opration 4:",op4
if op1>op2 and op1>op3 and op1>op4:
    print op1,"Is Maximum"
elif op2>op1 and op2>op3 and op2>op4:
    print op2,"Is Maximum"
elif op3>op1 and op3>op2 and op3>op4:
    print op3,"Is Maximum"
elif op4>op1 and op4>op2 and op4>op3:
    print op4,"Is Maximum"
if op1<op2 and op1<op3 and op1<op4:
    print op1,"Is Minimum"
elif op2<op1 and op2<op3 and op2<op4:
    print op2,"Is Minimum"
elif op3<op1 and op3<op2 and op3<op4:
    print op3,"Is Minimum"
elif op4<op1 and op4<op2 and op4<op3:
    print op4,"Is Minimum"
