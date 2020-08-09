n,p=map(int,input().split())
if n==1:
    print(p)
    exit()
elif p==1:
    print(1)
    exit()
elif n>60:最大公約数が2以上だとすると、60乗以上だと10**12を超えてしまうため、制約上最大公約数は１しか存在しない
    print(1)
    exit()
l=[]#Pの約数
for i in range(1,int(p**0.5)+1):
    if p%i==0:
        l.append(i)
#print(l)
s=[]
for i in range(len(l)):
    if l[i]**n<=p and p%(l[i]**n)==0:
        #print(l[i],l[i]**n)
        s.append(l[i])
    if l[i]**n>p:
        break
print(s[-1])
