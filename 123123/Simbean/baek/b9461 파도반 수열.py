#https://www.acmicpc.net/problem/9461
#https://www.acmicpc.net/problem/9461
import sys

def b9461():
    global p
    p = [0 for i in range(100)]
    p[0] = 1
    p[1] = 1
    p[2] = 1
    for i in range(3,100):
        p[i] = p[i-2] + p[i-3]
if __name__ == "__main__":
    b9461()
    #print(p)
    N = int(sys.stdin.readline())
    for i in range(N):
        M = int(sys.stdin.readline())
        print(p[M-1])
