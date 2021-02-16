import sys
#https://www.acmicpc.net/problem/11723
#https://www.acmicpc.net/problem/11723
if __name__ == "__main__":
    b = 0
    N = int(sys.stdin.readline())

    t = 0
    L = [0 for i in range(21)]

    for i in range(0,N):
        M = sys.stdin.readline().split()
        if len(M) > 1:
            index = int(M[1])
            if M[0] == "add":
                L[index] = 1
            elif M[0] == "check":
                print(L[index])
            elif M[0] == "remove":
                L[index] = 0
            elif M[0] == "toggle":
                if L[index] == 1:
                    L[index] = 0
                else:
                    L[index] = 1
        elif M[0] == "all":
            L = [1 for i in range(21)]

        elif M[0] == "empty":
            L = [0 for i in range(21)]