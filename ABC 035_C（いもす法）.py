# -*- coding: utf-8 -*-
"""
いもす法

長さnの要素がすべて0の配列Lの配列のうち、区間[l,r]について v加算する。
この操作をk回繰り返す。普通にやると、計算量が(r-l)*kとなってしまい、間に合わない。

そこで、操作ごとに、L[l]に+v、L[r+1]に-v の2点だけ処理を行う。
※r+1がn以上の場合は減算は行わず、L[l]の加算処理のみ行う

k回の処理が終わったら、累積和を求めれば、普通に区間[l,r]について v加算した場合と、同じ結果になる。
計算量はk~2kで済む

"""
"""
最初、numpyで区間[l,r]に一括加算しようとし、spyderで試したら普通に早かったので
numpyで提出してみたら、atcoderだとnumpy自体が激遅のためTLEになった。
"""

n,q=map(int,input().split())
lr=[list(map(int,input().split())) for _ in range(q)]
l=[0]*n
#print(l)
for i in range(q):#裏返った回数を加算する
    l[lr[i][0]-1]+=1
    if lr[i][1]<n:
        l[lr[i][1]]-=1

#print(l)
ans=""
tmp=0
for i in range(n):
    tmp+=l[i]
    l[i]=tmp
    if tmp%2==0:
        ans+="0"
    else:
        ans+="1"
print(ans)