#https://programmers.co.kr/learn/courses/30/lessons/60057
#https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    if len(s) == 1:
        answer = 1
    else:
        le = int(len(s)/2)
        index = 1
        word = [[] for i in range(le)]
        i = 0
        while True:
            if i+index <= len(s):
                word[index-1].append(s[i:i+index])
                i += index
            else:
                if s[i:] != '':
                    word[index-1].append(s[i:])
                if index >= le:
                    break
                i = 0
                index += 1
        wordlen = [0 for i in range(le)]
        index = -1
        for i in word:
            index += 1
            stack = 1
            for j in range(1,len(i)):
                if i[j-1] != i[j]:
                    if stack > 1:
                        w = len(str(stack))
                    else:
                        w = 0
                    wordlen[index] += (w+len(i[j-1]))
                    stack = 1
                else:
                    stack += 1
            if stack > 1:
                w = len(str(stack))
            else:
                w = 0
            wordlen[index] += (w+len(i[j]))
        answer = min(wordlen)
    return answer

if __name__ == "__main__":
    print(solution("aabbaccc"))