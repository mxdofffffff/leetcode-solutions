s = "anagram"
t = "nagaram"
def validAnagram(s, t):
    sl={}
    sl1={}
    if len(t)!=len(s):
        return False
    for char in s:
        if char in sl:
            sl[char]+=1
        else:
            sl[char]=1
    for char in t:
        if char in sl1:
            sl1[char]+=1
        else:
            sl1[char]=1
    return sl1==sl
print(validAnagram(s,t))