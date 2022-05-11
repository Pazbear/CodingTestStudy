import math
def solution(m, musicinfos):
    answer=None
    m = convertSharp(m)
    len_m = len(m)
    for musicinfo in musicinfos:
        start_t, end_t, music_name, music_code = musicinfo.split(',')
        t_def = timedef(start_t.split(':'), end_t.split(':'))
        music_code = convertSharp(music_code)
        music_code *= math.ceil(t_def/len(music_code))
        print(music_code)
        music_code = music_code[:t_def]
        print(music_code)
        
        if m not in music_code:
            continue
        
        if answer == None or answer[0] <t_def or (answer[0]==t_def and answer[1] >start_t):
            answer = (t_def, start_t, music_name)
    if answer:
        return answer[-1]
    else:
        return "(None)"
def timedef(start_t, end_t):
    return (int(end_t[0])*60+int(end_t[1]))-(int(start_t[0])*60+int(start_t[1]))

def convertSharp(str):
    return str.replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#",'g').replace("A#", 'a')