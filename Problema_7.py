n=int(input("Vârsta:"))
if n<20:
    dolari=1
    for x in range(1,n+1):
        dolari=(dolari*2)+x
    print(dolari,'$')
    dolari=1
    for x in range(1,n+1):
        dolari=(dolari*2)+x
        if dolari>100:
            print("La vârsta de",x,"ani cadoul a devenit mai mare de 100$")
            break
