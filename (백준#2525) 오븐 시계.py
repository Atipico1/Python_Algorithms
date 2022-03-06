hour, minute = map(int, input().split())
time = int(input())

result_minute = (minute + time % 60) % 60
result_hour = (hour + time // 60 + (minute + time % 60) // 60) % 24

print(result_hour, result_minute)
