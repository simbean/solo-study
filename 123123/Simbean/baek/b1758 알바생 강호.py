#https://www.acmicpc.net/problem/1758
#ttps://www.acmicpc.net/problem/1758
N = int(input())
tiplist = []
for i in range(0, N):
    tip = int(input())
    tiplist.append(tip)

tiplist.sort()
for i in range(N-1,-1,-1):
    tiplist[i] = tiplist[i] - ((N - 1)- i)
    if(tiplist[i] < 0 ):
        tiplist[i] = 0

    #print(tiplist)

print(sum(tiplist))