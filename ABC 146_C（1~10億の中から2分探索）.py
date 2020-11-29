# -*- coding: utf-8 -*-
"""
2分探索で1~10**9までの中からx以内に収まり、条件を満たす最大の値を見つける。

リストではないので、ライブラリではなく、自分で2分探索を組むこと。

最大を10**9 +1、最小を0にし、その中間の値をmidと定義し、
条件式でnのところにmidを代入して、whileの中で繰り返すことで、範囲を狭めていき、
最終的に最大と最小の差が1になったところのmidがnとなる。
"""
a,b,x=map(int,input().split())
if a>=x or b>=x:
    print(0)
    exit()
n1=10**9 +1
n2=0
while n1-n2>1:
    mid=(n1+n2)//2
    if a*mid+b*len(str(mid))<=x:
        n2=mid
    else:
        n1=mid
    #print(n1,n2,mid)
print(n2)