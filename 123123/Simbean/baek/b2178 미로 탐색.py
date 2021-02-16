#https://www.acmicpc.net/problem/2178

spaceN = input()
spaceN = spaceN.split()
space = []
visitroad = [[0,0]]
roadvalue = [[0,0]]
v = [0,0,0]
road = []
output: int = 1
N = int(spaceN[0])
M = int(spaceN[1])
for i in range(0, N):
    a = input()
    if len(a) == M:
        space.append(a)
    else:
        space = []
        break
point = 0
while 1:
    for i in range(0, len(roadvalue)):
            v = roadvalue[i]
            if v[0] == N-1 and v[1] == M-1:
               # print(6)
                point = 1
                break
            if v[0] < N-1 and space[v[0]+1][v[1]] == '1':
                road.append([v[0]+1, v[1]])
               # print(1)
            if v[0] > 0 and space[v[0]-1][v[1]] == '1':
                road.append([v[0]-1, v[1]])
                #print(2)
            if v[1] < M-1 and space[v[0]][v[1] + 1] == '1':
                road.append([v[0], v[1] + 1])
               # print(3)
            if v[1] > 0 and space[v[0]][v[1] - 1] == '1':
                road.append([v[0], v[1] - 1])
                #print(4)
            #print("a=" + str(road) + " v = " + str(roadvalue) + "t = " + str(sorted(visitroad)))
            j = 0
            while i == len(roadvalue)-1 and j < len(road):
                p = road[j]
                if j == road.index(p):
                    try:
                        a = visitroad.index(p)
                        road.remove(p)
                    except ValueError:
                            visitroad.append(p)
                            j += 1
                else:
                    road.remove(p)
            #print("1a=" + str(road) + " v = " + str(roadvalue) + "t = " + str(sorted(visitroad)))
            if i == len(roadvalue)-1:
                roadvalue = road
                output += 1
                #print("2a=" + str(road) + " v = " + str(roadvalue) + "t = " + str(sorted(visitroad)))
                road = []

    if point == 1:
        break
print(output)