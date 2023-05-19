import math as m
n1,n2=map(int,input().split())
HCF=m.gcd(n1,n2)
LCM = int((n1*n2)/(HCF))
print(LCM)