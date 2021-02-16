#https://programmers.co.kr/learn/courses/30/lessons/42840
#https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    list = [0,0,0]
    index = 0
    for i in answers:
        if i == a[index%5]:
            list[0] += 1
        if i == b[index%8]:
            list[1] += 1
        if i == c[index%10]:
            list[2] += 1
        index+= 1
    answer = []
    index = 1
    for i in list:
        if i == max(list):
            answer.append(index)
        index += 1
    return answer
if __name__ == "__main__":
    print(solution([1,2,3,4,5]))