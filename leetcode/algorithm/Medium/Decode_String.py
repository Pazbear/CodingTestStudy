class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if not stack:
                stack.append(c)
            elif c =="]":
                st = stack.pop()
                stack.pop()
                cnt = int(stack.pop())
                if not stack:
                    stack.append(cnt*st)
                elif stack[-1]=="[":
                    stack.append(cnt*st)
                else:
                    stack[-1]+=cnt*st
            elif c == '[':
                stack.append(c)
            elif (c.isalpha() and stack[-1].isalpha()) or (c.isdigit() and stack[-1].isdigit()):
                stack[-1]+=c
            else:
                stack.append(c)
        print(stack)
        return ''.join(stack)