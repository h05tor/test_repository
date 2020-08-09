"""
ある年のCODE FESTIVALの決勝では N問の問題が出題されました。
i(1≦i≦N)番目の問題の配点は i点です。

高橋くんは、このコンテストでちょうど N点を取りたいと思い、そのために解く問題の集合をどうするかを考えています。
配点が高い問題は難しいので、解く問題の配点のうちの最大値が最小になるようにしようと考えました。高橋くんが解くべき問題の集合を求めてください。


1,2,3....の累積和をベースに考えればよい。
累積和がNに一致してれば、そのままで良く、そうでない場合は何個かを+1ずつずらすことを考えればよい。
"""
n=int(input())
tmp=0
for i in range(1,10000000):
    tmp+=i
    if tmp>n:
        a=i-1
        tmp-=i
        break
    elif tmp==n:#
        for j in range(i):
            print(j+1)
        exit()
x=n-tmp#ずらす個数
y=a-x#ずらさない個数
#print(a,tmp,x,y)
ans=[]
for i in range(1,a+1):
    if i<=y:
        ans.append(i)
    else:
        ans.append(i+1)
#print(ans)
[print(i) for i in ans]
