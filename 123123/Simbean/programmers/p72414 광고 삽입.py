#https://programmers.co.kr/learn/courses/30/lessons/72414
def hmsconv(time):
    size = int(time[0:2])*(3600) + int(time[3:5])*(60) + int(time[6:])
    return size
def solution(play_time, adv_time, logs):
    answer = ""
    size = hmsconv(play_time)
    point = [0 for i in range(size+1)]
    #=====부분합=======
    for i in logs:
        j = i.split('-')
        t = hmsconv(j[0])
        if t >= 0:
            point[t] += 1
        t2 = hmsconv(j[1])
        if t2 != size+1:
            point[t2] -= 1
    for i in range(1,size+1):
        point[i] = point[i] + point[i-1]
    #=============
    #====뒤에 제일 큰값이 어느정도 있는지 판별 후 광고시간 - 큰 값을 앞부분에 채움==
    time = hmsconv(adv_time)
    result = [0 for i in range(size-time+1)]
    result[0] = sum(point[:time])
    for i in range(1,size-time+1):
        result[i] = -point[i-1] + result[i-1] + point[i+time-1]
    M = max(result)
    ans = result.index(M)
    #=====시간 표시부====
    hour = int(ans/3600)
    ans -= hour*3600
    if hour < 10:
        hour = '0' + str(hour)
    minute = int(ans/60)
    ans -= minute*60
    if minute < 10:
        minute = '0' + str(minute)
    sec = ans
    if sec < 10:
        sec = '0' + str(sec)
    answer = str(hour)+ ':' + str(minute) + ':' + str(sec)
    return answer
if __name__ == "__main__":
    print(solution("02:03:55",	"00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))