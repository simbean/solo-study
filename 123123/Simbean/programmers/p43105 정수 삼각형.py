#https://programmers.co.kr/learn/courses/30/lessons/43105
#https://programmers.co.kr/learn/courses/30/lessons/43105
#https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    answer = 0
    dplist =[]
    dplist.append(triangle[0][0] + triangle[1][0])
    dplist.append(triangle[0][0] + triangle[1][1])
    del triangle[0]
    del triangle[0]
    #print(dplist)
    for i in triangle:
        Maxlist = []
        Maxlist.append(dplist[0] + i[0])
        for j in range(1,len(dplist)):
            if dplist[j-1] > dplist[j]:
                Maxlist.append(dplist[j-1]+i[j])
            else:
                Maxlist.append(dplist[j]+i[j])
        Maxlist.append(dplist[-1] + i[-1])
        dplist = Maxlist[:]
        #print(dplist)
    answer = max(dplist)
    return answer
if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))