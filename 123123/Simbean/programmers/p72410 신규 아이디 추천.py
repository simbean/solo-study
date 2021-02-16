#https://programmers.co.kr/learn/courses/30/lessons/72410
#https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = ''
    pass2 = ''
    for a in new_id:
        i = a.lower()
        if i == '-' or i == '_' or i == '.' or 'a'<=i <= 'z' or '0'<= i <= '9':
            pass2 += i.lower()
    prev = pass2[0]
    pass3 = pass2[0]
    pass2 = pass2[1:]
    for b in pass2:
        if prev == '.' and b == '.':
            pass
        else:
            pass3 += b
        prev = b
    pass4 = pass3[:]
    if pass3[0] == '.':
        pass4 = pass4[1:]
    if pass3[-1] == '.':
        pass4 = pass4[:-1]
    if pass4 == '':
        answer = 'aaa'
    elif len(pass4) == 2:
        answer = pass4 + pass4[-1]
    elif len(pass4) == 1:
        answer = pass4 * 3
    elif len(pass4) > 15:
        answer = pass4[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    else:
        answer = pass4[:]
    return answer
if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))