#https://programmers.co.kr/learn/courses/30/lessons/72411
#https://programmers.co.kr/learn/courses/30/lessons/72411
#https://programmers.co.kr/learn/courses/30/lessons/72411

import itertools as it
def solution(orders, course):
    answer = []
    dic = {}
    for a in course:
        ans = {}
        dic = {}
        for i in orders:
            items = []
            for j in i:
                items.append(j)
            lis = list(it.combinations(items,a))
            for k in lis:
                word = ''.join(sorted(k))
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word]  = 1
        for i in dic:
            if dic[i] >1:
                ans[i] = dic[i]
        ans = sorted(ans.items(),reverse = True, key=lambda x:x[1])
        if ans == []:
            continue
        prev = ans[0][1]
        #print(prev)
        for i in ans:
            if prev == i[1]:
                answer.append(i[0])
            else:
                break
        #print(ans)
    answer.sort()
    return answer

if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]	))