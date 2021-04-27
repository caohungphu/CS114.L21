import textwrap

try:
    txt = input()
    n = int(input())
except:
    n = 83
txt_out = []
i = 0
while txt[i]== ' ':
    i+=1
txt_ = txt[i:]
words = txt_.splitlines(' ')
i=0
print(words)
length_ = len(words) -1
while i <= length_: 
    if len(words[i]) >= n:
        print(*words[i],sep='')
        i+=1
    else:
        txt_ = []
        length = len(words[i])
        txt_.append(words[i])
        while True :
            if(i<length_):
                i+=1
                length += len(words[i])
                if length >= n:
                    break  
                else:   
                    txt_.append(words[i])   
            else:
                 i+=1
                 break
        print(*txt_,sep='')
