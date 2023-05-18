p,r,t=map(int,input().split())
ci=p*pow(1+(0.01*r),t)
print(format(ci,'.2f'))