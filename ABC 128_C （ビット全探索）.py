"""
on と off の状態を持つ N個の スイッチと、
M個の電球があります。スイッチには1からNの、電球には1からMの番号がついています。

電球iはki個のスイッチに繋がっており、スイッチsi1,si2,...,sikiのうち on になっているスイッチの個数を 
2で割った余りが piに等しい時に点灯します。

全ての電球が点灯するようなスイッチの on/off の状態の組み合わせは何通りあるでしょうか。
"""
"""
・スイッチの全組み合わせのビット文字列を生成し、0をOFF、1をONとする
・各電球に関係するスイッチが何個ONになっているか探索し、2で割った余りがpiかどうかでその電球がONかどうか判定する
・点灯している電球の数がM個であれば、ansに1加算する
"""
N,M = map(int,input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int,input().split()))
ans=0
for i in range(2**N):
    b="0"*(N-len(bin(i)[2:]))+bin(i)[2:]
    #print(b)
    on=0
    for j in range(M):#各電球ごと　#電球1はスイッチ1,2,5のうち奇数個ついていればよい
        c=0#その電球に必要なスイッチの数用のカウント
        for k in range(N):
            if k+1 in ks[j][1:]:#例えばスイッチ1が電球1に必要なスイッチのリストふ含まれているとき
                if b[k]=="1":
                    c+=1
        if c%2==p[j]:
            on+=1
    if on==M:
        ans+=1
print(ans)
