n=int(input("n:"))
suma=0
for x in range(3,n):
    for y in range(1,n):
        if y<=x:
            if x%y==0 and x!=y:
                suma+=y
            if x==y:
                if suma==x:
                    print(x)
                    suma=0
                elif suma!=x:
                    suma=0
        elif y>x:
            continue
