from math import *
A=float(input("A="))
B=float(input("B="))
n=int(input("n="))
x=(B-A)/n
for i in range(1,n):
    fx=1-sin(A+i*x)
    print(fx)