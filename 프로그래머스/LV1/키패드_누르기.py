def solution(numbers, hand):
    answer = ''
    leftloc, rightloc = [0,3], [2,3]
    for number in numbers:
        if (number-1)%3==0:
            answer+='L'
            leftloc = getLoc(number)
        elif number !=0 and  (number-1)%3==2:
            answer+='R'
            rightloc = getLoc(number)
        else:
            numloc = getLoc(number)
            leftdiff = abs(numloc[0]-leftloc[0])+abs(numloc[1]-leftloc[1])
            rightdiff = abs(numloc[0]-rightloc[0])+abs(numloc[1]-rightloc[1])
            print(number,numloc,leftloc, rightloc, leftdiff, rightdiff)
            if leftdiff < rightdiff:
                answer+='L'
                leftloc=numloc
            elif leftdiff > rightdiff:
                answer+='R'
                rightloc=numloc
            else:
                if hand=='left':
                    answer+='L'
                    leftloc=numloc
                else:
                    answer+='R'
                    rightloc=numloc
    return answer

def getLoc(number):
    if number==0:
        return [1,3]
    return [(number-1)%3, (number-1)//3]