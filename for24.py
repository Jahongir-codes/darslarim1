n=int(input("n="))
x=float(input("x="))
s=1
k=1
for i in range(1,2*n+2):
    k*=i
    if i%2==0:
        s+=x**i/k*(-1)*(-1)**(i)//2
print(s)