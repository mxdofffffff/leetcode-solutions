ransomNote = "aa"
magazine = "ab"
def ransom(ransomNote,magazine):
    sl={}
    sl1={}
    for char in magazine:
        if char in sl:
            sl[char] += 1
        else:
            sl[char] = 1
    for char in ransomNote:
        if char in sl1:
            sl1[char] += 1
        else:
            sl1[char] = 1
    for key,value in sl1.items():
        if key not in sl:
            return False
        if sl[key]<value:
            return False
    return True
print(ransom(ransomNote,magazine))