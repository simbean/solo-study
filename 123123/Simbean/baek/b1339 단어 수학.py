# This is a sample Python script.
import operator
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#https://www.acmicpc.net/problem/1339
#https://www.acmicpc.net/problem/1339
#https://www.acmicpc.net/problem/1339
#https://www.acmicpc.net/problem/1339
#https://www.acmicpc.net/problem/1339

def makeList(wordList):
    global dic
    dic = {}
    for i in range(0,len(wordList)):
        for j in range(0,len(wordList[i])):
            try:
                dic[wordList[i][j]]+=10**(len(wordList[i]) - j-1)
            except KeyError:
                dic[wordList[i][j]] = 10**(len(wordList[i]) - j-1)
    list = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)
    return list
if __name__ == '__main__':
    N = int(input())
    L = []
    selectInt = 9
    output = 0
    for i in range(0,N):
        M = input()
        L.append(M)
    priority = makeList(L)
    for i in range(0,len(priority)):
        output += selectInt * priority[i][1]
        selectInt -= 1
    print(output)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
