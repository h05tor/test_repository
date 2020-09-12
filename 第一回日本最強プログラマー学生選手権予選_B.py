"""
・A内の転倒数を求め、BはAをk個くっつけた数列なので、kをかける
・AとAの間の転倒数を k*(k-1)/2かける

2つ目については例えばAが　10 9 8 7 5 6 3 4 2 1の場合
A内の転倒数は43であるに対し、AとAの間の転倒数は45であることに注意
"""
n,k=map(int,input().split())
a=list(map(int,input().split()))
#a内部ての転倒数
c_1=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            c_1+=1
ans1=c_1*k
#print(ans1)
#aとaの間の転倒数
c_2=0
for i in range(n):
    for j in range(n):
        if a[i]>a[j]:
            c_2+=1
ans2=c_2*(k*(k-1)//2)
print((ans1+ans2)%(7+10**9))
