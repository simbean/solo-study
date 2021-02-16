#https://programmers.co.kr/learn/courses/30/lessons/42885
#https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people)-1
    while True:
        if a > b:
            break
        answer += 1
        if people[a] + people[b] <= limit:
            a += 1
        b -= 1
    return answer
if __name__ == "__main__":
    print(solution([70, 50, 80, 50],	100))