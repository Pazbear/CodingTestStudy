def solution(dartResult):
    dart_arr=[]
    temp_str=""
    for dart in dartResult:
        if dart.isdecimal():
            temp_str+=dart
        elif dart == 'S':
            dart_arr.append(int(temp_str))
            temp_str=""
        elif dart == 'D':
            dart_arr.append(int(temp_str)**2)
            temp_str=""
        elif dart == 'T':
            dart_arr.append(int(temp_str)**3)
            temp_str=""
        elif dart == '*':
            dart_arr[-1]*=2
            if len(dart_arr)!=1:
                dart_arr[-2]*=2
        elif dart == '#':
            dart_arr[-1]*=-1
    return sum(dart_arr)