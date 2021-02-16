NM = input()
#https://www.acmicpc.net/problem/1783
N = int(NM.split()[0])
M = int(NM.split()[1])
if N < 3:
    if N == 1:
        print(1)
    elif M > 6:
        print(4)
    else:
        print(int((M+1)/2))
elif 4 <= M < 7:
    print(4)
elif M < 4:
    print(M)
else:
    print(M-2)