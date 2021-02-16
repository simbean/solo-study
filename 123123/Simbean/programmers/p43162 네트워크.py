#https://programmers.co.kr/learn/courses/30/lessons/43162
#https://programmers.co.kr/learn/courses/30/lessons/43162
#https://programmers.co.kr/learn/courses/30/lessons/43162
#https://programmers.co.kr/learn/courses/30/lessons/43162
#https://programmers.co.kr/learn/courses/30/lessons/43162
#https://programmers.co.kr/learn/courses/30/lessons/43162
#네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크네트워크
def __init__(a,b):
    global Numberarray,visitarray
    global Num
    Num = int(a)
    Numberarray = b
    visitarray = []

def Network():
    output = 0
    for a in range(0, Num):
        if a in visitarray:
            continue
        else:
            visitarray.append(a)
            for index in visitarray:
                array = Numberarray[index]
                for i in range(0, len(array)):
                    if array[i] == 1:
                        if not i in visitarray:
                            visitarray.append(i)
        output += 1
    return output

def solution(n, computers):
    __init__(n, computers)
    answer = Network()
    return answer

if __name__ == "__main__":
    answer = solution(6, [[1, 1, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1]])
    print(answer)