word1="observe"
word2="see"

wc={}
is_kangaroo=True

for c in word1:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

for ch in input:
    if ch in wc and wc[ch]>0:
        wc[ch]-=1
    else:
        is_kangaru=False
        break
print(ch)

