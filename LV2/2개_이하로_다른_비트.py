def solution(numbers):
    answer = []
    for number in numbers:
        number = int(number)
        b_number = bin(number)
        for i in range(len(b_number)-1, -1, -1):
            if b_number[i] != '1':
                temp = int(2**(len(b_number)-i-2))
                answer.append(number + (temp if temp >0 else 1))
                break
    return answer