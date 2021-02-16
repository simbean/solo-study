#https://www.acmicpc.net/problem/10815
#https://www.acmicpc.net/problem/10815
#https://www.acmicpc.net/problem/10815
#https://www.acmicpc.net/problem/10815

if __name__ == "__main__":
    N = int(input())
    N1= input()
    N1 = list(map(int, N1.split(' ')))
    N1.sort()
    M = int(input())
    M1= input()
    M1 = list(map(int, M1.split(' ')))
    #print(N1)
    for i in M1:
        flag = 0
        s = 0
        e = N-1
        while s <= e:
            index = int((e + s) / 2)
            Mid = N1[index]
            #print(Mid)
            if Mid == i:
                flag = 1
                print(1, end=' ')
                break
            elif Mid > i:
                e = index - 1
            else:
                s = index + 1
        if flag != 1:
            print(0, end=' ')

