n=int(input("n="))
x=float(input("x="))
s=0
for i in(1,2*n+2,2):
    if i%2==1:
        s+=x**i/i*(-1)**(i-1)//2
print(s)