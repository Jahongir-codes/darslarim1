n=int(input("n="))
s=0
for i in range(n):
    s+=(11+i)/10*(-1)**i
print(s)