numarator1,numitor1=int(input("numărător:")),int(input("numitor  :"))
numarator2,numitor2=int(input("numărător:")),int(input("numitor  :"))
intreg=0
operatie1='adunare'
operatie2='înmulțire'
print("soluția adunării=")
if numitor1!=numitor2:
    numarator=numarator1*numitor2+numarator2*numitor1
    numitor=numitor1*numitor2
    if numarator>numitor:
        if numarator%numitor==0:
            print(int(numarator/numitor))
        elif numarator%numitor!=0:
            for x in range(2,10):
                if numarator%x==0 and numitor%x==0:
                    numarator=numarator/x
                    numitor=numitor/x
            if numarator>numitor:
                if numitor==1:
                    print(int(numarator))
                else:
                    while numarator>numitor:
                        numarator-=numitor
                        intreg+=1
                    print(intreg,'intreg și',int(numarator),'/',int(numitor))
    elif numarator<numitor:
        for x in range(2,10):
            if numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        print(int(numarator),'/',int(numitor))
elif numitor1==numitor2:
    numarator=numarator1+numarator2
    numitor=numitor1
    if numarator<numitor:
        for x in range(2,10):
            if numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        print(int(numarator),'/',int(numitor))
    elif numarator>numitor:
        for x in range(2,10):
            if numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        if numarator>numitor:
            if numitor==1.0:
                    print(int(numarator))
            else:
                while numarator>numitor:
                    numarator-=numitor
                    intreg+=1
                print(intreg,'intreg și',int(numarator),'/',int(numitor))
print("soluția înmulțirii=")
numarator=numarator1*numarator2
numitor=numitor1*numitor2
if numarator==numitor:
    print(1)
elif numarator!=numitor:
    if numarator<numitor:
        for x in range(2,10):
            if numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        print(int(numarator),'/',int(numitor))
    if numarator%numitor==0:
        print(int(numarator/numitor))
    elif numarator%numitor!=0:
        for x in range(2,10):
            if numarator%x==0 and numitor%x==0:
                numarator=numarator/x
                numitor=numitor/x
        if numarator>numitor:
            if numitor==1:
                print(int(numarator))
            else:
                while numarator>numitor:
                    numarator-=numitor
                    intreg+=1
                print(intreg,'intreg și',int(numarator),'/',int(numitor))