#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    for i in range(0, len(reserve)):
        if reserve[i] in lost:
            lost.remove(reserve[i])
            reserve[i] = -100

    reserve.sort()
    answer = n - len(lost)
    for i in reserve:
        if lost == []:
            break
        if i - 1 in lost:
            lost.remove(i - 1)
            answer += 1
        elif i + 1 in lost:
            lost.remove(i + 1)
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))