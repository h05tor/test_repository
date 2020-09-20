# -*- coding: utf-8 -*-
"""
現在時刻と空港A,Bの時刻表を参照しながら、i,jを進めていく
2重whileになるが、i,jは前回終了地点から進めるので計算量はO(N)になる
どちらかの空港で終電を過ぎてしまった時点で終了となる
"""
n,m=map(int,input().split())
x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=0#往復数
t=0#現在時刻
i=0#Aの時刻表の何番目を参照しているか
j=0#Bの時刻表の何番目を参照しているか
while (i<n and j<m):
    while True:
        if t>a[i]:
            i+=1
            if t>a[-1]:#Aの終電を過ぎる
                print(ans)
                exit()
        else:
            t=a[i]#乗る
            t+=x#Bに着く
            break
    while True:
        if t>b[j]:
            j+=1
            if t>b[-1]:#Bでの終電を過ぎる
                print(ans)
                exit()
        else:
            t=b[j]#乗る
            t+=y#Aに着く
            break
    ans+=1#1往復完了
print(ans)
            