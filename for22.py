n=int(input("n="))
x=float(input("x="))
s=1
k=1
for i in range(1,n+1):
    k*=i
    s+=pow(x,i)/k
print(s)
