print "Enter A Conversion Type:\n1.Feet To Inch\n2.Inch To Feet\n3.Feet To Meter\n4.Meter To Feet"
n=input("Enter A Choice:")
v=input("Enter A Value:")
sc={
    1:str('Feet To Inch:')+str(float(v)*12),
    2:str('Inch To Feet:')+str(float(v)/12),
    3:str('Feet To Meter:')+str(float(v)/3.281),
    4:str('Meter To Feet:')+str(float(v)*3.281),
}
print sc.get(n,"There Is No Such Choice!")
