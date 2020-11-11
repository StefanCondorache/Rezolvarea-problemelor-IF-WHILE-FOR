a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    if a==b and a==c:
        print("Echilateral")
    elif (a==b) or (a==c) or (b==c):
        print("Isoscel")
    else:
        print("Scalen")
else:
    print("nu există triunghi")