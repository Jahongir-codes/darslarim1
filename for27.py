n=int(input("n="))
x=float(input("x="))
s=0
toq=1
juft=1
for k in range(0,n+1):
    if k>0:
        toq*=2*k-1
        juft*=2*k
    daraja=2*k+1
    had=toq*x**daraja/(juft*(2*k+1))
    s+=had
print(s)