from collections import Counter

word = list((input().upper()))
dic = Counter(word) # Counter 클래스를 이용해서 (문자,빈도) 쌍의 딕셔너리 생성
result = []
for key, value in dic.items():  # dic loop 돌면서 value값이 최대이면 result에 저장
    if value == max(dic.values()):
        result.append(key) 
 
if len(result) == 1: # result의 원소가 한개이면, key값 프린트, 아니면 ? 프린트
    print(result[0])
else:
    print('?')
