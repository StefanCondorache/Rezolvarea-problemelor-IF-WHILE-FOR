n=int(input("n="))
if n>1:
    total=0
    factorial=1
    for x in range(1,n+1):
        factorial*=x
        total+=factorial
    print("suma =",total)
