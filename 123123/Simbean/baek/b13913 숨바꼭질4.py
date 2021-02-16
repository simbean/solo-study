#https://www.acmicpc.net/problem/13913
import sys
if __name__ == "__main__":
    global ans,clone
    L = [100001 for i in range(0 , 100001)]
    M = []
    ans = 0
    N = list(map(int,sys.stdin.readline().split()))
    L[N[0]] = 0
    prev = []
    M.append(N[0])
    stack = []
    while True:
        clone = []
        if L[N[1]] != 100001:
            break
        ans += 1
        for i in M:
            if i+1 <= 100000 and L[i+1] == 100001:
                L[i+1] = ans
                clone.append(i+1)
            if i-1 >= 0 and L[i-1] == 100001:
                L[i-1] = ans
                clone.append(i - 1)
            if i*2 <= 100000 and L[i*2] == 100001:
                L[i*2] = ans
                clone.append(2 * i)
        M = clone[:]
        prev.append(M)
    point = N[1]
    stack = [N[1]]
    if N[0] != N[1]:
        for i in range(len(prev)-2,-1,-1):
            if point - 1 in prev[i]:
                point -= 1
            elif point + 1 in prev[i]:
                point += 1
            elif point % 2 == 0:
                if int(point/2) in prev[i]:
                    point = int(point/2)
            stack.append(point)
        stack.append(N[0])
    stack.reverse()
    print(L[N[1]])
    for i in stack:
        print(i, end =' ')