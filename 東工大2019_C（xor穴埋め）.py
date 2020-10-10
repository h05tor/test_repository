n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
#print(a)
"""
まず、-1以外の要素をxorする。
"""
for i in range(n):
    if a[i]>=0:
        ans=ans^a[i]
        #print(ans)
#print(ans^x)
"""
-1が含まれていない場合は、全要素のxorがXに等しいかどうかだけ確認
・正しければaをリストを外してそのまま出力
・Xでなければ-1を出力
"""
if a.count(-1)==0:
    if ans==x:
        print(*a)
        exit()
    else:
        print(-1)
        exit()
"""
-1が含まれている場合（穴埋めが必要な場合）
穴埋めの回数が1回で済むような場合（-1以外の要素のxor値 xor X がXより小さい)
は2つめ以降の-1は0埋めできる。

-1以外の要素のxor値 xor X がXより大きい場合は、X埋めし、残りの-1があれば、そのうち0に落ち着く。
残りの-1がなければ解が存在しないので-1を出力
"""
c=0
d=0
t=a.count(-1)
#print(ans,ans^x)
for i in range(n):
    if a[i]==-1:
        if d==0:
            if ans^x<=x:
                a[i]=ans^x
                d=1
            else:
                if c<=t:
                    a[i]=x
                    ans^=x
                    c+=1
                else:
                    print(-1)
                    exit()
            
        else:
            a[i]=0
z=0
for i in range(n):
    z^=a[i]
if z==x:    
    print(*a)
else:
    print(-1)