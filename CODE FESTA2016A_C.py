"""
K回操作を行う
1回操作をするごとにアルファベットがa→bのように進む　zの場合はaに戻る
この操作でできる辞書順最小の文字列を出力


最初の文字から優先的にaにする。
aにした、もともとa、残りのKでaにできない場合は次の文字に進む。
最後の文字で残りのKを使い切る
"""
s=input()
k=int(input())
n=len(s)
i=0
ans=""
while i<n:
    if i!=n-1:
        if s[i]=="a":
            ans+="a"
            #print(ord(s[i]),123-ord(s[i]),k)
        elif k>=123-ord(s[i]):
            ans+="a"
            k-=(123-ord(s[i]))
            #print(ord(s[i]),123-ord(s[i]),k)
        else:
            ans+=s[i]
            #print(ord(s[i]),123-ord(s[i]),k)
    else:
        if k>=123-ord(s[i]):
            k-=(123-ord(s[i]))#一旦aにする
            k=k%26
            ans+=chr(97+k)
        else:
            ans+=chr(ord(s[i])+k)
        
    i+=1
print(ans)
