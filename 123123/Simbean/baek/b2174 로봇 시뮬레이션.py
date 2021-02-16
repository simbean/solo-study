#https://www.acmicpc.net/problem/2174
import collections as C
import sys
global rx
global ry
rx = [1, 0, -1, 0]
ry = [0, 1, 0, -1]  # left E,N,W,S
class Robot:
    global space
    def __init__(self,x,y,d,index):
        self.index = index
        self.x = x-1
        self.y = y-1
        space[self.y][self.x] = self.index
        if d == 'E':
            self.d = 0
        elif d == 'N':
            self.d = 1
        elif d == 'W':
            self.d = 2
        elif d == 'S':
            self.d = 3
    def orders(self, order):
        if order == 'F':
            space[self.y][self.x] -= self.index
            self.x += rx[self.d]
            self.y += ry[self.d]
            if self.x < 0 or self.x >= N[0] or self.y < 0 or self.y >= N[1]:
                print(f'Robot {self.index} crashes into the wall')
                exit(0)
            elif space[self.y][self.x] != 0:
                print(f'Robot {self.index} crashes into robot {space[self.y][self.x]}')
                exit(0)
            space[self.y][self.x] += self.index
        elif order == 'L':
            self.d = (self.d+1) % 4
        elif order == 'R':
            self.d = (self.d - 1) % 4
def b2174(map, order):
    global space
    r = [0 for i in range(M[0])]
    index = 1
    space = [[0 for _ in range(N[0])] for j in range(N[1])]
    for i in map:
        r[index-1] = Robot(i[0],i[1],i[2],index)
        index += 1
    deq = C.deque([])
    for i in order:
        while i[2] != 0:
            deq.append([i[0],i[1]])
            i[2] -= 1
    #print(deq)
    while len(deq) != 0:
        O = deq.popleft()
        #print(O)
        r[O[0]-1].orders(O[1])
        #print(space)
    print('OK')
if __name__ == "__main__":
    global N,M
    N = list(map(int,sys.stdin.readline().split()))
    M = list(map(int, sys.stdin.readline().split()))
    Map = []
    order = []
    for i in range(M[0]):
        p =list(sys.stdin.readline().split())
        Map.append([int(p[0]),int(p[1]),p[2]])
    many = 0
    for i in range(M[1]):
        p = list(sys.stdin.readline().split())
        orders = int(p[2])
        order.append([int(p[0]),p[1],orders])
    b2174(Map,order)