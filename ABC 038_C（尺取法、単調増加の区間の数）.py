"""
尺取法

単調増加の区間の数を求める

単調増加が途切れるまたは終端でansに
（区間の長さ+1）*(区間の長さ)//2を足していく
"""
n=int(input())
a=list(map(int,input().split()))
i=0
j=0
ans=0
while j<n:
    if j!=n-1:
        if a[j]<a[j+1]:
            j+=1
        else:
            ans+=(j-i+2)*(j-i+1)//2
            j+=1
            i=j
    else:
        ans+=(j-i+2)*(j-i+1)//2
        j+=1
        i=j
print(ans)
