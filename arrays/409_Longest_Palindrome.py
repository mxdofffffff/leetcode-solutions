s = "abccccdd"
def longpalindrom(s):
    result=0
    sl={}
    odd = False
    for char in s:
        if char in sl:
            sl[char]+=1
        else:
            sl[char]=1
    for key,value in sl.items():
        if value % 2 == 0:
            result+=value
        else:
            result += value - 1
            odd = True
    if odd == True:
        result+=1
    return result


print(longpalindrom(s))