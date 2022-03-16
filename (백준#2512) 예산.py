import sys
n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())
result = []
def solution(money):
    sum = 0
    for i in L:
        if i > money:
            sum += money
        else:
            sum += i
    return sum

if budget >= sum(L):
    print(max(L))
    
else:          
    start = 0 # start를 min(L)로 잡으면 ValueError 발생 (WHY?)
    last = max(L)

    while start <= last:
        
        mid = (start + last) // 2
        if solution(mid) > budget:
            last = mid - 1
        elif solution(mid) < budget:
            result.append(mid)
            start = mid + 1
        else:
            result.append(mid)
            break
    print(max(result))
