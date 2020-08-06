"""
リーダーより西にいて西を向いている人の数と
リーダーより東にいて東をむいている人の数の合計の最小値を求める

まず最初に東を向いている人の数をcount関数で求め、全体の数Nからそれを引いたものを西を向いている人の数

"""

N=int(input())
S=input()
e=S.count("E")#東を向いている人の数
w=N-e#西を向いている人の数
ans=10**9
for i in range(N):
    left=i
    right=N-1-i
    if i==0:
        left_e=0
        left_w=0
        if S[i]=="E":
            right_e=e-1
            right_w=w
        else:
            right_e=e
            right_w=w-1
    else:
        if S[i-1]=="E":
            left_e+=1
        elif S[i-1]=="W":
            left_w+=1
        if S[i]=="E":
            right_e-=1
        elif S[i]=="W":
            right_w-=1
    tmp=left_w+right_e
    #print(left,left_e,left_w,right,right_e,right_w,tmp)
    if ans>tmp:
        ans=tmp
print(ans)
