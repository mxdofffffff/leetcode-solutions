s = "Hello Worldfdfsfsf 1"
def lengthOfLastWord(s):
    s = s.strip().split()
    return len(s[-1])
print(lengthOfLastWord(s))
