import sys
#https://www.acmicpc.net/problem/10816
#https://www.acmicpc.net/problem/10816
#https://www.acmicpc.net/problem/10816
#https://www.acmicpc.net/problem/10816
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    N1 = sys.stdin.readline().split()
    N1 = list(map(int, N1))
    M = int(sys.stdin.readline())
    M1 = sys.stdin.readline().split()
    M1 = list(map(int, M1))
    dic = {}
    for i in N1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in M1:
        if i in dic:
            print(dic[i], end=' ')
        else:
            print(0, end = ' ')
