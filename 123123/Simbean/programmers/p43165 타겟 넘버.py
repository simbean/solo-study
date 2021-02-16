#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    nlist = []
    nlist.append(numbers[0])
    nlist.append(-numbers[0])
    del numbers[0]
    for i in numbers:
        nlistclone = []
        for j in nlist:
            nlistclone.append(j + i)
            nlistclone.append(j - i)
        nlist = nlistclone[:]
    print(nlist)
    for i in nlist:
        if i == target:
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution([1, 1, 1], -1))