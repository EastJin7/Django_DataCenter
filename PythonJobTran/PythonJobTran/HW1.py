#1題
import random
count=10000
arr = [0,0,0,0,0,0]
brr = [0,0,0,0,0,0]
while count >0:
    count-=1
    x = random.randrange(1,7)
    arr[x-1]+=1
for i in range(0,6):
    brr[i]=arr[i]/100
    print("擲出 "+str(i+1)+" 共"+str(arr[i])+"次，佔比"+str(brr[i])+"%")

#2題
x=0.0 #追加行
Y=6
Z=12.3
x=float(Y)+Z #追加行
print(type(x))

#3題
sum=0
for i in range(0,1001,2):
    if (i%2==0):
        sum+=i
print(sum)

#4題
sum=0
i=1
while (sum<=3000)&(i<=1000):
    if (i%2==1):
        sum+=i
        i+=2
print(sum)