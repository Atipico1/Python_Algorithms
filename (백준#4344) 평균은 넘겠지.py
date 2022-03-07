n = int(input()) # 반복 수 입력

for _ in range(n):
    # num에는 학생 수, score에는 점수 할당
    L = list(map(int, input().split())) 
    num = L[0]
    score = L[1:]
    mean = sum(score) / num
    count = 0
    # 평균을 넘을때마다 count에 1추가
    for i in L[1:]:
        if i > mean:
            count += 1
            
    print(f'{round(count/num*100, 3):.3f}%')
