"""
高橋君は、互いに区別出来る N本の棒を持っています。
i本目の棒の長さは Liです。

高橋君は、これらのうち 3本の棒を使って三角形を作ろうとしています。このとき、棒の長さを 
a,b,cとして、以下の条件がすべて成り立たなければなりません。
a<b+c
b<c+a
c<a+b
作れる三角形は何種類あるでしょうか。ただし、
2つの三角形は、そのうち一方にのみ使われている棒が存在するときに異なるとします。


制約
入力は全て整数
3≤N≤2×10^3
1≤Li≤10^3
"""
"""
制約上限が2000であるため、O(N3)だと間に合わない
まず、ソートして一番大きいのと2番目に大きいのだけをforで回し、固定（O(N2)）
ソートされているため、一番短いもので条件を満たす棒の範囲は限られるため、2分探索
"""

import bisect
n=int(input())
a=list(map(int,input().split()))
a.sort()
#print(a)
ans=0
for i in range(n-1,1,-1):
    for j in range(i-1,0,-1):
        t=bisect.bisect_right(a,a[i]-a[j])
        #print(a[i],a[j],a[i]-a[j],t,j-t)
        if j-t>0:
            ans+=j-t
print(ans)
        
