#https://programmers.co.kr/learn/courses/30/lessons/42578
#https://programmers.co.kr/learn/courses/30/lessons/42578
#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    for i in dic.items():
        answer *= i[1]+1
    return answer -1
if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))