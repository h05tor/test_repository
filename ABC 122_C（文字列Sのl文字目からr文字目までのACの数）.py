"""
A, C, G, T からなる長さ 
Nの文字列Sが与えられます。以下のQ個の問いに答えてください。

問 i(1≤i≤Q): 整数li,ri(1≤li<ri≤N) が与えられる。
Sの先頭から li文字目からri文字目までの (両端含む) 部分文字列を考える。この文字列に AC は部分文字列として何回現れるか。

制約
2≤N≤10^5
1≤Q≤10^5
Sは長さNの文字列である。
Sの各文字は A, C, G, T のいずれかである。
1≤li<ri≤N
"""
"""
文字列Sのi文字目以降にACが何個あるかを最初にカウントしていく
"""

n,q=map(int,input().split())
s=input()
l=[0]*n
tmp=0
for i in range(n-2,-1,-1):
    if s[i:i+2]=="AC":
        tmp+=1
    l[i]+=tmp
#print(l)
for i in range(q):
    L,R=map(int,input().split())
    print(l[L-1]-l[R-1])
