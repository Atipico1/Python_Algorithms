# 단순히 X in Y 연산자로 해결할 경우 time limit을 초과
# binary Search로 찾아야함

import sys
n = int(sys.stdin.readline())
L = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
L2 = list(map(int, sys.stdin.readline().split()))

for target in L2:
    a = 0
    first, last = 0, n-1
    
    while first <= last:
        mid = (first + last) // 2
        if target == L[mid]:
            a = 1
            break
        elif target < L[mid]:
            last = mid - 1
        else:
            first = mid + 1

    if a:
        print(1)
    else:
        print(0)
