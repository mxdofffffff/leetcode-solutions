s = "bg"
t = "ahbgdc"
def subsequence(s,t):
    p = 0
    if len(s)<0:
        return True
    for char in t:
        if char == s[p]:
            p+=1
        if p == len(s):
            return True
    return False
print(subsequence(s,t))
