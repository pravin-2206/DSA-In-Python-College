num=125
sum=0
n=num
while(num>0):
        sum=sum*10+(num%10)
        num=num//10
if(num==n):
        print("Prime number")
else:
        print("Not prime")