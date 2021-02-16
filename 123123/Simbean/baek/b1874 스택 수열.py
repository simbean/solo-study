#n 배열 arr의 크기
#1부터 오름차순으로 배열이 있다고 가정할때 스택을 사용하여
#주어진 arr과 똑같이 만들 수 있는지 true false 반환
#https://www.acmicpc.net/problem/1874
def sol(N, Mlist):
    index = 1
    stack = []
    for i in range(0, len(Mlist)):
        while True:
            if index > Mlist[i]:
                break
            stack.append(index)
            index += 1
        #print(stack) #스택 안 진행과정 확인할수 있음
        if stack[-1] == Mlist[i]:
            del stack[-1]
        else:
            return False
    return True
if __name__ == '__main__':
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    N = int(input())
    M = input()
    Mlist = list(map(int, M.split()))
    output = sol(N,Mlist)
    print(output)
