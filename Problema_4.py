from fractions import Fraction
numarator1,numitor1=int(input("numărător:")),int(input("numitor  :"))
numarator2,numitor2=int(input("numărător:")),int(input("numitor  :"))
print("soluția adunării=",Fraction(numarator1,numitor1)+Fraction(numarator2,numitor2))
print("soluția înmulțirii=",Fraction(numarator1,numitor1)*Fraction(numarator2,numitor2))
