#https://www.acmicpc.net/problem/2217
#https://www.acmicpc.net/problem/2217
#https://www.acmicpc.net/problem/2217
#https://www.acmicpc.net/problem/2217

weight = []
small = 10000
weight_final = []
rope_many = int(input())
for i in range(0, rope_many):
    weight_a = int(input())
    weight.append(weight_a)
weight.sort()
for i in range(0, len(weight)-1):
    weight_final.append(int(weight[i]) * (len(weight)-i))
weight_final.append(weight[-1])
weight_final.sort()
print(weight_final[-1])