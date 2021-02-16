#https://programmers.co.kr/learn/courses/30/lessons/42579
#https://programmers.co.kr/learn/courses/30/lessons/42579
#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dic = {}
    many = {}
    index = -1
    for i in genres:
        index += 1
        if i in dic:
            if plays[index] > plays[dic[i][0]]:
                dic[i].insert(0,index)
            else:
                try:
                    if plays[index] <= plays[dic[i][1]]:
                        many[i] += plays[index]
                        continue
                except IndexError:
                    pass
                dic[i].insert(1,index)
            if len(dic[i]) > 2:
                del dic[i][-1]
            many[i] += plays[index]
        else:
            dic[i] = [index]
            many[i] = plays[index]
            print(index)
    print(dic)
    print(many)
    a = sorted(many.items(), key=lambda x : x[1],reverse = True)
    for i in a:
        answer += dic[i[0]]
    return answer
if __name__ == "__main__":
    print(solution(["A", "A", "B", "A"],[5, 5, 6, 5]))