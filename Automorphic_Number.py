n=int(input())
sq=n*n
mod=pow(10,len(str(n)))
if sq%mod==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")