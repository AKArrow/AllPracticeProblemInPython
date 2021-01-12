def ctf(val):
    return float((val*9/5)+32)
def ftc(val):
    return float((val-32)*5/9)
print "Enter Yor Choice:\n1.Celsius To Fahrenheit\n2.Fahrenheit To Celsius"
a=input("Enter Your Choice:")
v=input("Enter Your Value:")
if a==1:
    print "Conversion:",ctf(v)
else:
    print "Conversion:",ftc(v)