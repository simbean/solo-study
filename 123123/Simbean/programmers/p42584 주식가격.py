#https://programmers.co.kr/learn/courses/30/lessons/42584
#https://programmers.co.kr/learn/courses/30/lessons/42584
#https://programmers.co.kr/learn/courses/30/lessons/42584
#https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    cul = []
    culclone = []
    answer = []
    index = 0
    for i in prices:
        culclone = []
        for j in cul:
            answer[j] += 1
            if prices[j] <= i:
                culclone.append(j)
        cul = culclone[:]
        cul.append(index)
        answer.append(0)
        index += 1
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))