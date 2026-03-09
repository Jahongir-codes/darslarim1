n=int(input("n="))
x=float(input("x="))
s=1
toq=1
juft=1
for k in range(1,n+1):
    juft*=2*k
    if k>1:
        toq*=2*k-3
    had=(-1)**(k+1)*toq*x**k/(juft)
    s+=had
print(s)