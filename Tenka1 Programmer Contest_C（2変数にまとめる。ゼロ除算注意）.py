"""
整数 Nが与えられる。
4/N = 1/h + 1/n + 1/wを満たす正整数 
h,n,wを求めよ。

条件を満たす解が複数ある場合、どれを出力しても良い。

制約
Nに対して h,n,w≤3500となる解が存在することが保証される。
"""

"""
Nは整数として与えられ、wを式変形すると2変数にできるので、計算量をO(N^2)にできる
0除算エラーに注意

python3だと間に合わない可能性があるのでpypyで提出

"""
N=int(input())
# 4hnw=Nnw+Nhw+Nhn
# 4hnw-Nnw-Nhw=Nhn
#w=Nhn/(4hn-Nn-Nh)
for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-N*n-N*h==0:
            continue
        if N*h*n%(4*h*n-N*n-N*h)==0:
            w=N*h*n//(4*h*n-N*n-N*h)
        else:
            continue
        if 4*h*n*w==N*(n*w+h*w+h*n) and w>0:
            print(h,n,w)
            exit()
