#https://programmers.co.kr/learn/courses/30/lessons/64065
#https://programmers.co.kr/learn/courses/30/lessons/64065
#https://programmers.co.kr/learn/courses/30/lessons/64065
import json
def solution(s):
    answer = []
    s = s.replace("{","[")
    s = s.replace("}","]")
    s = json.loads(s)
    s = sorted(s, key = lambda x : len(x))
    for i in s:
        for j in i:
            if not j in answer:
                answer.append(j)
    return answer
if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
