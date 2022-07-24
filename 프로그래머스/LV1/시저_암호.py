from string import ascii_uppercase, ascii_lowercase
def solution(s, n):
    answer = ''
    uppercase_converter, lowercase_converter = dict(), dict()
    for i in range(len(ascii_uppercase)):
        uppercase_converter[ascii_uppercase[i]]=ascii_uppercase[(i+n)%26]
        lowercase_converter[ascii_lowercase[i]]=ascii_lowercase[(i+n)%26]
    for c in s:
        if c==' ':
            answer+=c
        elif c.isupper():
            answer+=uppercase_converter[c]
        else:
            answer+=lowercase_converter[c]
    return answer