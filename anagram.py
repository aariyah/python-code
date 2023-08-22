word1=input("enter a string")
word2=input("enter another string")

srt_word1=sorted(word1)
srt_word2=sorted(word2)
print(srt_word1)
print(srt_word2)
print("anagram" if srt_word1==srt_word2 else "not an anagram")
