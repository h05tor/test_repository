n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
x=0#b[i]より大きいa[i]の数
y=0#b[i]より小さいa[i]の数
z=0#負数の総和
for i in range(n):
    if a[i]>=b[i]:
        x+=1
        l.append(a[i]-b[i])
    else:
        y+=1
        z+=a[i]-b[i]
l.sort(reverse=True)
#b[i]より大きいa[i]の中から、a[i]-b[i]が大きいものから順に移し替えていけば最小にできる
if x==n:
    print(0)
    exit()
ans=y
for i in range(x):
    z+=l[i]
    ans+=1
    if z>=0:
        print(ans)
        exit()
if z<0:
    print(-1)
