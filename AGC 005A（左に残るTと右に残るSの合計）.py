"""
文字列 Xが与えられます。Xの長さは偶数であり、半分は S 、もう半分は T からなります。

高橋君は ST という文字列が苦手です。なので以下の操作を10^10000回行うことにしました。

Xの(連続な)部分文字列で ST となるもののうち、最も左側にあるものを取り除く。存在しないならば何もしない。
最終的に Xは何文字になるかを求めてください。
"""
"""
左側に追いやられたTと右側に追いやられたSは消せずに残ることに着目
左側から順にSの連続区間、Tの連続区間をカウントしT→Sに切り替わったときにそれぞれの連続分に着目し、Tの方が多かったら、消せずに残るTが出る
また最後の文字についてカウントする際、Sが連続している状態で終わった場合、Tが右に来ないためこの連続したSも消されずに残る
"""

s=input()
ans=0
i=0
c=-1
tmp1=0#Sが連続した数
tmp2=0
x=0
y=0
while i<len(s):
    if c==-1:
        if s[i]=="S":
            tmp1=1
            c=0
        else:
            tmp2+=1
            c=1
    elif c==0:
        if s[i]=="S":
            tmp1+=1
        else:
            tmp2+=1
            c=1
    elif c==1:
        if s[i]=="S":
            if tmp1>=tmp2:
                tmp1=tmp1-tmp2
                tmp2=0
            else:
                y+=tmp2-tmp1
                tmp2=0
                tmp1=0
            c=0
            tmp1+=1
        else:
            tmp2+=1
    if i==len(s)-1:
        if tmp1>=tmp2:
            x+=tmp1-tmp2
            tmp2=0
        else:
            y+=tmp2-tmp1
            tmp1=0
    i+=1
    
    #print(ans,tmp1,tmp2,x,y)
print(x+y)
