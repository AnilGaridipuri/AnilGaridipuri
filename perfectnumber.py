c=int(input("enter value of c"))
s=0
for i in range(1,c):
    if(c%i==0):
        s=s+i
if(c==s):
    print(c,"is a perfect number.")
else:
    print(c,"is not a prefect number.")