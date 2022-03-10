# 모든 경우에 대해 brute force를 할 경우 time limit을 초과함
# 적절한 lan의 길이가 한정 돼있으므로(랜선 중 가장 긴선)
# 1부터 max(lan)까지를 binary search해서, 조건을 만족시키는 값 중 최대값을 구하면 됨

import sys
m, n = map(int, sys.stdin.readline().split())
lan = []
for _ in range(m):
    lan.append(int(sys.stdin.readline()))
    
result = []
first, last = 1, max(lan)

while first <= last:
    mid = (first + last) // 2
    count = 0 
    for i in lan:
        count += i // mid
    
    if count < n:
        last = mid - 1
    else:
        first = mid + 1
        result.append(mid)

print(max(result))
