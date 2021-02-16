#https://www.acmicpc.net/problem/2437
#https://www.acmicpc.net/problem/2437
#https://www.acmicpc.net/problem/2437
def s2437_init():
    global N,M
    N = int(input())
    M = input()
    M = M.split()
    M = list(map(int, M))
    M.sort()
def s2437_plus():
    listA = []
    sumM = 0
    for i in range(0,len(M)):
        sumM += M[i]
        listA.append(sumM)
    if M[0] != 1:
        print(1)
    else:
        s2437_Compare(listA)
def s2437_Compare(List):
    sum = 0
    aws = 0
    for i in range(0, len(List)):
        try:
            if List[i]+1 < M[i+1]:
                aws = List[i]+1
                break
        except IndexError:
            aws = List[-1]+1
    print(aws)
if __name__ == "__main__":
    s2437_init()
    #print(N)
    #print(M)
    s2437_plus()