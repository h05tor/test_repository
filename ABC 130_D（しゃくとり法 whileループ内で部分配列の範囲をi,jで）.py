# -*- coding: utf-8 -*-
"""
長さNの正整数列 A=a1,a2,…,aNと整数Kが与えられます。
Aの連続する部分列であって、以下の条件を満たすようなものは何個あるでしょうか。

(条件) 連続部分列に含まれる全ての要素の値の和はK以上である。
ただし、ある二つの連続部分列が列として同じでも、取り出された位置が異なるならそれらは別々に数えるものとします。

出力が 
32bit整数型に収まらない場合があることに注意してください。

制約
1≦ai≦10^5
1≦N≦10^5
1≦K≦10^10
入力は以下の形式で標準入力から与えられます。
N K

a1 a2 ... aN

出力
条件を満たすような連続部分列の個数を出力してください。

入力例
4 10
6 1 2 7
出力例
2
A[1..4]=a1,a2,a3,a4(要素の値の和は 16)
A[2..4]=a2,a3,a4(要素の値の和は10)の二通りです。


"""

n,k=map(int,input().split())
a=list(map(int,input().split()))
i=0
j=1
tmp=a[0]
ans=0
while True:
    #print(tmp,i,j)
    if tmp<k:
        if j==n:
            break
        else:
            j+=1
            tmp+=a[j-1]
    else:
        ans+=(n-j+1)#tmp=a[i:j]が、k以上の場合、jがそれ以上の場合についても満たすので、j=j~nの分をすべて足す
        if j-i>1:
            i+=1
            tmp-=a[i-1]
        else:
            if j==n:
                break
            else:
                i+=1
                j+=1
                tmp=tmp+a[j-1]-a[i-1]

print(ans)
