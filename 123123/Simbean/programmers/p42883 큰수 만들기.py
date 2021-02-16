#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    stack = 0
    index = 0
    for j in range(1000000 * 1000000):
        j -= index
        if j < 0 :
            j = 0
        if number[j] < number[j+1]:
            number = number[:j] + number[j+1:]
            j -= 1
            stack += 1
            index += 2
        elif j == len(number)-2:
            number = number[:-1]
            stack += 1
            index += 2
        if stack == k:
            break
    answer = number
    return answer
if __name__ == "__main__":
    print(solution("4177252841", 4))