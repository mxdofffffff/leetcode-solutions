x=122
def palindrome(x):
    x=str(x)
    if x == x[::-1]:
        return True
    else:
        return False
print(palindrome(x))