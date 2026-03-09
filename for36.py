N=int(input("N="))
K=int(input("K="))
s=0
for i in range(1,N+1):
    l=1
    for j in range(K):
        l*=i
    s+=l
print(s)

