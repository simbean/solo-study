#https://www.acmicpc.net/problem/1463
count = 0
cnt = 0
array = {}
def s1463_init():
    Num = int(input())
    return Num
def s1463_analysis(ans):
    global array
    array[1] = 0
    for i in range(2, ans + 1):
        Num1 = 100001
        Num2 = 100001
        Num3 = 100001
        if i % 3 == 0:
            Num1 = array[i / 3] + 1
        if i % 2 == 0:
            Num2 = array[i / 2] + 1
        Num3 = array[i-1] + 1
        array[i] = min(Num1,Num2,Num3)
def main():
    a = s1463_init()
    cnt = s1463_analysis(a)
    print(array[a])
