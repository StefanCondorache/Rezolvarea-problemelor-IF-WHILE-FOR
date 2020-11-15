n=int(input("n:"))
s1,s2=0,0
suma_c=0
suma_p=0
#a
for x in range(1,n+1):
    suma_p=x**3
    s1+=suma_p
    suma_c+=x
s2=suma_c**2
if s1<s2:
    print("s1<s2")
elif s1>s2:
    print("s1>s2")
else:
    print("s1=s2")
#b
s1,s2=0,0
suma_c=0
suma_p=0
for x in range(1,n+1):
    suma_p+=x**2
    suma_c+=x
s1=suma_p*3
s2=suma_c+n**3+n**2
if s1<s2:
    print("s1<s2")
elif s1>s2:
    print("s1>s2")
else:
    print("s1=s2")
