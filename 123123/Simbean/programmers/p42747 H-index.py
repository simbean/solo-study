#https://programmers.co.kr/learn/courses/30/lessons/42747
#https://programmers.co.kr/learn/courses/30/lessons/42747
#https://programmers.co.kr/learn/courses/30/lessons/42747
#https://programmers.co.kr/learn/courses/30/lessons/42747


def sortmap(citations):
    index = len(citations)
    for i in citations:
        if i >= index:
            return index
        else:
            index -= 1
    return index
def solution(citations):
    citations.sort()
    print(citations)
    answer = sortmap(citations)
    print(answer)
    return answer

if __name__ == "__main__":
    solution([3, 0, 6, 1, 5])