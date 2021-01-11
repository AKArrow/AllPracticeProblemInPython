print "Enter A Conversion Type:\n1.Feet To Inch\n2.Inch To Feet\n3.Feet To Meter\n4.Meter To Feet"
n=input("Enter A Choice:")
v=input("Enter A Value:")
sc={
    1:float(v)*12,
    2:float(v)/12,
    3:float(v)/3.281,
    4:float(v)*3.281
}
print sc.get(n,"There Is No Such Choice!")