#https://programmers.co.kr/learn/courses/30/lessons/17677
#https://programmers.co.kr/learn/courses/30/lessons/17677
#https://programmers.co.kr/learn/courses/30/lessons/17677
def Jacard(L):
    minL = []
    maxL = L[0][:]
    Temp1 = L[0][:]  # 긴거
    Temp2 = L[1][:]  # 짧은거
    for i in Temp1:
        if i in Temp2:
            minL.append(i)
            del Temp2[Temp2.index(i)]
    Temp2 = L[1][:]
    for i in Temp2:  # maxL 초기값이 긴거이므로
        if i in Temp1:  # 중복일경우
            del Temp1[Temp1.index(i)]
            pass
        else:
            maxL.append(i)
    A = len(minL)
    B = len(maxL)
    #print(minL)
    #print(maxL)
    if A == 0 and B == 0:
        A = 1
        B = 1
    return (A / B * 65536)

def solution(str1, str2):
    L1 = []
    L2 = []
    for i in range(0, len(str1) - 1):
        if ord('a') <= ord(str1[i].lower()) <= ord('z') and ord('a') <= ord(str1[i + 1].lower()) <= ord('z'):
            L1.append(str1[i:i + 2].lower())

    for i in range(0, len(str2) - 1):
        if ord('a') <= ord(str2[i].lower()) <= ord('z') and ord('a') <= ord(str2[i + 1].lower()) <= ord('z'):
            L2.append(str2[i:i + 2].lower())

    L3 = [L1, L2]
    answer = Jacard(L3)
    return int(answer)
if __name__ == "__main__":
    print(solution("FRANCE","french"))
