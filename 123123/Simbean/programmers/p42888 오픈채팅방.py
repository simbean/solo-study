#https://programmers.co.kr/learn/courses/30/lessons/42888
#https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    dic = {}
    L = []
    for i in record:
        L.append(i.split())
    for i in L:
        try:
            dic[i[1]] = i[2]
        except IndexError:
            pass
    for i in L:
        if i[0] == 'Enter':
            answer.append(f"{dic[i[1]]}님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(f"{dic[i[1]]}님이 나갔습니다.")
    return answer
if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))