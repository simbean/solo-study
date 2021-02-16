#https://www.acmicpc.net/problem/11399
#https://www.acmicpc.net/problem/11399
#https://www.acmicpc.net/problem/11399
def s11399_init():
    global Needs
    People = int(input())
    Need = input()
    Needs = Need.split()
    if People == len(Needs):
        Needs = list(map(int, Needs))
    else:
        pass
def s11399_make():
    sum = 0
    result = 0
    Needs.sort()
    for i in range(0, len(Needs)):
        sum = Needs[i] + sum
        result += sum
    return result
def main():
    s11399_init()
    output = s11399_make()
    print(output)
