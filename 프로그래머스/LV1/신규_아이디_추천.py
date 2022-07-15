def solution(new_id):
    answer = ''
    dot = False
    new_id = new_id.lower()
    new_id=list(new_id)

    for i in range(len(new_id)):
        if not new_id[i].isalpha() and not new_id[i].isdecimal() and new_id[i]!='-' and new_id[i]!='_' and new_id[i]!='.':
            new_id[i]=""
    new_id=list(''.join(new_id))
    for i in range(len(new_id)):
        if new_id[i]=='.':
            for j in range(i+1, len(new_id)):
                if new_id[j]=="":
                    continue
                elif new_id[j]=='.':
                    new_id[j]=''
                else:
                    break
    new_id=list(''.join(new_id))
    if new_id[0]=='.':
        new_id=new_id[1:]
    if new_id and new_id[-1]=='.':
        new_id=new_id[:-1]
    if not new_id:
        new_id = ["a"]
    if len(new_id)>15:
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id=new_id[:-1]
    while len(new_id)<3:
        new_id.append(new_id[-1])
    return ''.join(new_id)