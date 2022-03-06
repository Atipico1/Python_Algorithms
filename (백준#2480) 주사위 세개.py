nums = list(map(int, input().split()))
result = 0
for i in range(1, 7):
    if nums.count(i) == 3:
        result = 10000+i*1000
    if nums.count(i) == 2:
        result = 1000+i*100
        
if result:
    print(result)
else:
    print(max(nums)*100)
