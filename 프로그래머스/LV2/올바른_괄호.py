def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
    return not stack