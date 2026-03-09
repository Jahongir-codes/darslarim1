n=int(input("n="))
s=1
k=1
for i in range(1,n+1):
    k*=i
    s+=1/k
print(s)