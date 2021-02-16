#https://www.acmicpc.net/problem/11779
import collections as d
import sys
def b11779(n,m,inform,s,e):
    deq = d.deque([[s,0]])
    pay = []
    for i in range(1, n+1):
        deq.append([i,float('inf')])
        pay.append([i,float('inf')])
    pay[s-1][1] = 0
    load = [[] for i in range(n)]
    load[s-1] = [s]
    while len(deq) != 0:
        point = deq.popleft()
        if point[0] in dic:
            for i in dic[point[0]]:
                cost = point[1] + i[1]
                if cost <= pay[i[0]-1][1]:
                    pay[i[0] - 1][1] = cost
                    deq.appendleft([i[0],cost])
                    l = load[point[0]-1] + [i[0]]
                    load[i[0]-1] = l
    print(pay[e-1][1])
    print(len(load[e-1]))
    for i in load[e-1]:
        print(i,end=' ')
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    inform = 1
    dic = {}
    for i in range(0, m):
        bus = list(map(int,sys.stdin.readline().split()))
        if bus[0] in dic:
            dic[bus[0]].append([bus[1],bus[2]])
        else:
            dic[bus[0]] = [[bus[1],bus[2]]]
        '''if bus[1] in dic:
            dic[bus[1]].append([bus[0],bus[2]])
        else:
            dic[bus[1]] = [[bus[0],bus[2]]]'''
    t = list(map(int, sys.stdin.readline().split()))
    s = t[0]
    e = t[1]
    b11779(n,m,dic,s,e)
