numarator1,numitor1=int(input("numărător:")),int(input("numitor  :"))
numarator2,numitor2=int(input("numărător:")),int(input("numitor  :"))
intreg=0
if numitor1==numitor2:
    numarator=numarator1+numarator2
    numitor=numitor1
    if numarator==numitor:
        print("soluția adunării=",1)
    elif numarator<numitor:
        for x in range(2,10):
            while numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        print("soluția adunării=",int(numarator),'/',int(numitor))
    elif numarator>numitor:
        while numarator>numitor:
            numarator-=numitor
            intreg+=1
        for x in range(2,10):
            while numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        print("soluția adunării=",intreg,'întreg și',int(numarator),'/',int(numitor))
elif numitor1!=numitor2:
    numarator=numarator1*numitor2+numarator2*numitor1
    numitor=numitor1*numitor2
    if numarator==numitor:
        print("soluția adunării=",1)
    elif numarator<numitor:
        for x in range(2,10):
            while numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        print("soluția adunării=",int(numarator),'/',int(numitor))
    elif numarator>numitor:
        while numarator>numitor:
            numarator-=numitor
            intreg+=1
        for x in range(2,10):
            while numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        print("soluția adunării=",intreg,'întreg și',int(numarator),'/',int(numitor))
numarator=numarator1*numarator2
numitor=numitor1*numitor2
if numarator==numitor:
    print("soluția înmulțirii=",1)
elif numarator<numitor:
    for x in range(2,10):
        while numarator%x==0 and numitor%x==0:
            numarator=numarator/x
            numitor=numitor/x
    print("soluția înmulțirii=",int(numarator),'/',int(numitor))
elif numarator>numitor:
    while numarator>numitor:
        numarator-=numitor
        intreg+=1
    for x in range(2,10):
        while numarator%x==0 and numitor%x==0:
            numarator=numarator/x
            numitor=numitor/x
    print("soluția înmulțirii=",intreg,'întreg și',int(numarator),'/',int(numitor))