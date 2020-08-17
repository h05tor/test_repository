import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
#print(a)
ans=10**10
for i in range(n-1):
    GCD=math.gcd(a[i],a[i+1])
    if ans>GCD:
        ans=GCD
print(ans)
