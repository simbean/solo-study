#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    phone_book.sort()
    phone_list = {}
    for i in phone_book:
        if i[0] in phone_list:
            phone_list[i[0]].append(i) 
        else:
            phone_list[i[0]] = [i]
    print(phone_list)
    for i in phone_list.items():
        if len(i[1]) > 1:
            for j in range(0,len(i[1])):
                for k in range(0,len(i[1])):
                    if i[1][k] == i[1][j][0:len(i[1][k])] and j != k:
                        return False
    return answer
if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))