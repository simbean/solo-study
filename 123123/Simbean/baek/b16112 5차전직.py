#https://www.acmicpc.net/problem/16112
count = 0
cnt = 0
array = {}
def s16112_init():
    global N,M
    Num = input()
    N = int(Num.split()[0])
    M = int(Num.split()[1])
    Num2 = input()
    val = Num2.split()
    val = list(map(int, val))
    val.sort()
    return val
def main():
    unitResult = 0
    Result = 0
    val = s16112_init()
    unitResult = sum(val)
    for i in range(0,M):
        unitResult -= val[i]
        #print('unitResult = ' + str(unitResult))
        Result += unitResult
    print(Result)
