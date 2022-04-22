n=int(input("Enter no. to check if it is armstrong "))
o=n
i=0
while(n!=0):
    y=n%10
    i=i+y**3
    n=n//10
if(o==i):
    print("no. is armstrong")
else:
    print("no. is not armstrong")
