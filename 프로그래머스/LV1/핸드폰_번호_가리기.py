def solution(phone_number):
    return ''.join([ '*' if i <len(phone_number)-4 else phone_number[i] for i in range(len(phone_number))])