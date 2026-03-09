N=int(input("N="))
s=0
for i in range(1,N+1):
    l=1
    for j in range(N+1-i):
        l*=i
    s+=l
print(s)

