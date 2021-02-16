#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    weight = int((brown-8)/2 )
    reverse = 0
    answer= [3 + weight, 3+reverse]
    for i in range(0,weight):
        if (weight+1) * (reverse+1) == yellow:
            break
        else:
            answer[0] -= 1
            answer[1] += 1
            weight -= 1
            reverse += 1        
    return answer
if __name__ == "__main__":
    print(solution(10, 2))