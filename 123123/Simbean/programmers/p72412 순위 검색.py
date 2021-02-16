#https://programmers.co.kr/learn/courses/30/lessons/72412
#https://programmers.co.kr/learn/courses/30/lessons/72412
"""시간초과남
def solution(info, query):
    answer = []
    applicant = {0 : [] ,1: [],2: [],3: [],4: []}
    dic = {'python' : [] , 'java' : [],'cpp' : [], 'backend': [],'frontend': [], 'junior': [],'senior': [],'chicken': [],'pizza': [], '-': []}
    for i in info:
        word = i.split(' ')
        applicant[0].append(word[0])
        applicant[1].append(word[1])
        applicant[2].append(word[2])
        applicant[3].append(word[3])
        applicant[4].append(word[4])
    dic['-'] = range(len(applicant[0]))
    for i in range(4):
        for j in range(len(applicant[0])):
            dic[applicant[i][j]].append(j)
    for i in query:
        word = i.split(' ')
        word = [word[0],word[2],word[4],word[6],word[7]]
        p = range(len(applicant[0]))
        for j in range(4):
            p = set(p).intersection(dic[word[j]])
        p = list(p)
        clone = []
        for j in p:
            if int(applicant[4][j]) >= int(word[4]):
                clone.append(j)
        p = clone[:]
        answer.append(len(p))
    return answer

"""
def solution(info, query):
    answer = []
    applicant = {0: [], 1: [], 2: [], 3: [], 4: []}
    dic = {'python': [], 'java': [], 'cpp': [], 'backend': [], 'frontend': [], 'junior': [], 'senior': [],
           'chicken': [], 'pizza': [], '-': []}
    for i in info:
        word = i.split(' ')
        applicant[0].append(word[0])
        applicant[1].append(word[1])
        applicant[2].append(word[2])
        applicant[3].append(word[3])
        applicant[4].append(word[4])
    dic['-'] = range(len(applicant[0]))

    for i in range(4):
        for j in range(len(applicant[0])):
            dic[applicant[i][j]].append(j)
    t1 = ['python', 'java', 'cpp', '-']
    t2 = ['backend', 'frontend', '-']
    t3 = ['junior', 'senior', '-']
    t4 = ['chicken', 'pizza', '-']
    result = {}
    for j1 in range(4):
        for j2 in range(3):
            w1 = set(dic[t1[j1]]).intersection(dic[t2[j2]])
            for j3 in range(3):
                w2 = w1.intersection(dic[t3[j3]])
                for j4 in range(3):
                    w3 =  list(w2.intersection(dic[t4[j4]]))
                    if w3 != []:
                        l = []
                        for k in list(w2.intersection(dic[t4[j4]])):
                            l.append(int(applicant[4][k]))
                        result[str(t1[j1])+str(t2[j2])+str(t3[j3])+str(t4[j4])]= sorted(l)
                    else:
                        result[str(t1[j1]) + str(t2[j2]) + str(t3[j3]) + str(t4[j4])] = []
    for i in query:
        word = i.split(' ')
        p = result[str(word[0]) + str(word[2]) + str(word[4]) + str(word[6])]
        score = int(word[7])
        s = 0
        e = len(p)-1
        while s<=e:
            Mid = int((s+e)/2)
            if p[Mid] < score:
                s = Mid+1
            else:
                e = Mid-1
        answer.append(len(p)-s)
    return answer
if __name__ == "__main__":
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],	["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))