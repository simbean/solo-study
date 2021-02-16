#https://programmers.co.kr/learn/courses/30/lessons/64061
#https://programmers.co.kr/learn/courses/30/lessons/64061
#https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    queue = []
    for i in moves:
        for j in range(0,len(board[0])):
            if board[j][i-1] != 0:
                queue.append(board[j][i-1])
                board[j][i-1] = 0
                #print(queue)
                if len(queue) >= 2 and queue[-1] == queue[-2]:
                    del queue[-1]
                    del queue[-1]
                    answer+= 2
                break
    return answer
if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
