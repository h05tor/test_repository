# -*- coding: utf-8 -*-
"""
日付ごとに移動可能な範囲が与えられるので進める時に進めるだけ進める

スタート地点と目的地の町番号の大小によって進行方向異なるので場合分けすること
"""
n,d,k=map(int,input().split())
lr=[list(map(int,input().split())) for _ in range(d)]
st=[list(map(int,input().split())) for _ in range(k)]
#print(lr)
#print(st)
for i in range(k):
    ans=0#日数
    x=st[i][0]#現在地
    y=st[i][1]#目的地
    if x<y:
        for j in range(d):
            ans+=1
            if lr[j][0]<=x<=lr[j][1]:#移動可能な場合
                if y<=lr[j][1]:#目的地が移動可能範囲にある場合
                    print(ans)
                    break
                else:
                    x=lr[j][1]
    else:
        for j in range(d):
            ans+=1
            if lr[j][0]<=x<=lr[j][1]:#移動可能な場合
                if y>=lr[j][0]:#目的地が移動可能範囲にある場合
                    print(ans)
                    break
                else:
                    x=lr[j][0]
                    