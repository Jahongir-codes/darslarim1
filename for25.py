n=int(input("n="))
x=float(input("x="))
s=0
for i in(1,n+1):
    s+=x**i/i*(-1)**i
print(s)