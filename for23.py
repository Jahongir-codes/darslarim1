n=int(input("n="))
x=float(input("x="))
s=0
k=1
for i in range(1,2*n+2):
    k*=i
    if i%2==1:
        s+=x**i/k*(-1)**(i-1)//2
print(s)