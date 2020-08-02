"""
英小文字からなる文字列 Sが与えられます。 
Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで 
S=Tとすることができるか判定してください。
Tの末尾に dream dreamer erase eraser のいずれかを追加する。
"""
S=input()
s=len(S)
T=""
i=0
while True:
    if S[i:i+5]=="dream":
        if i+5==s or S[i+5:i+7]!="er":
            T+="dream"
            i+=5
        elif S[i+5:i+7]=="er":
            if i+7==s or S[i+7]!="a":
                T+="dreamer"
                i+=7
            else:
                T+="dream"
                i+=5
    elif S[i:i+6]=="eraser":
        T+="eraser"
        i+=6
    elif S[i:i+5]=="erase":
        T+="erase"
        i+=5
    else:
        print("NO")
        exit()
    #print(T)
    if len(T)>=len(S):
        break
print("YES")
