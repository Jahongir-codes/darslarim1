n=int(input("n="))
a=float(input("a="))
k=1
s=1
for i in range(1,n+1):
    k*=a
    s+=k
print(s)