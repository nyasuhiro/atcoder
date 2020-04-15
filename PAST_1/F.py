input_str=input()

strFlg=False

ansList=[]

tmpStr=""

for i in range(len(input_str)):
    if input_str[i].isupper():
        if strFlg==False:
            strFlg=True
            tmpStr=""+input_str[i]
        else:
            strFlg=False
            tmpStr+=input_str[i]
            ansList.append(tmpStr)
    else:
        tmpStr+=input_str[i]

print(*sorted(ansList,key=str.lower),sep="")
