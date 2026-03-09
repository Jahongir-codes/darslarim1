N=int(input("N="))
s=0
for i in range(1,N+1):
    l=1
    for j in range(1,i+1):
        l*=i
    s+=l
print(s)

