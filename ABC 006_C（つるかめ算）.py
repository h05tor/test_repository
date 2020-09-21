"""
mがnの2~3倍の場合は赤ちゃんが0人
mがnの3~4倍の場合は成人が0人で固定すればよい

mがnの2倍未満または4倍より多い場合は、-1 -1 -1と出力すればよい
"""
n,m=map(int,input().split())
if m<n*2 or m>n*4:
    print(-1,-1,-1)
    exit()
if m>=n*2 and m<=n*3:
    x=n
    y=0
    z=0
    while True:
        if 2*x+3*y==m:
            print(x,y,z)
            exit()
        x-=1
        y+=1
else:
    x=0
    y=n
    z=0
    while True:
        if 3*y+4*z==m:
            print(x,y,z)
            exit()
        y-=1
        z+=1
