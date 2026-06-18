s = "()[]"
def validparentheses(s):
    stack = []
    map = {")":"(", "]":"[", "}":"{"}
    for char in s:
        if char in map:
            if stack:
                top = stack.pop()
            else:
                top = "-"
            if map[char]!=top:
                return False
        else:
            stack.append(char)
    return len(stack) == 0
print(validparentheses(s))