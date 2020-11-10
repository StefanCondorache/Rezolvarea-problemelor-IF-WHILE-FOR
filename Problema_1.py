luna=[28,29,30,31]
n=int(input("n="))
if n in luna:
    if n==luna[0]:
        print("Februarie")
    elif n==luna[2]:
        print("Aprilie,Iunie,Septembrie,Noiembrie")
    elif n==luna[3]:
        print("Ianuarie,Martie,Mai,Julie,August,Octombrie,Decembrie")
    elif (n==luna[1]):
        anul=int(input("anul:"))
        if anul%4==0:
            print("februarie")
        else:
            print("inexistent")
else:
    print("inexistent")