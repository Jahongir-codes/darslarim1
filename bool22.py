n=int(input("n="))
a=n//100
b=n//10%10
c=n%10
print(c<b<a or c>b>a)
