# -*- coding: utf-8 -*-
"""
高橋くんは N個の品物を1個ずつ順番に買う予定です。
i番目に買う品物の値段はAi円です。
高橋くんは M枚の割引券を持っています。

品物を買う際に割引券を好きな枚数使うことができます。
X円の品物を買う際にY枚の割引券を使った場合、その品物を 
X/(2^Y)円(小数点以下切り捨て)で買うことができます。
最小で何円あれば全ての品物を買うことができるでしょうか。

1≤N,M≤10^5
1≤Ai≤10^9
"""
"""
まず、リストＡを正負反転させてからをヒープキュー（優先度付きキュー）に変換し、
（正負反転のため）最小値を取り出していき、2で割って（切り下げ）てからヒープキューに戻す

最後にヒープキューの要素の和を求め、正負を再度反転させ元に戻したものがans

"""
import heapq

n,m=map(int,input().split())
A=list(map(int,input().split()))
#print(A)
for i in range(n):
    A[i]*=-1
#print(A)
heapq.heapify(A)
for i in range(m):
    x=heapq.heappop(A)
    #print(x,A)
    if x%2==0:
        x//=2
    else:
        x=x//2 +1
    heapq.heappush(A,x)
    #print(A)
ans=-1*sum(A)
print(ans)
