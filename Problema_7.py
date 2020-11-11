n=int(input("Vârsta:"))
if n<20:
    suma=1
    dolari=1
    for x in range(1,n+1):
        dolari*=2
        suma+=dolari+x
    print("suma=",suma)
    suma=1
    dolari=1
    for x in range(1,n+1):
        dolari*=2
        suma+=dolari+x   
        if suma>100:
            print("La vârsta de",x,"ani cadoul a fost mai mare de 100$")
            break
    