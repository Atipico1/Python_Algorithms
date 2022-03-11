# loop를 통해 해결하려 할경우 time limit exceed
# 따라서 나눗셈을 통해 한 번에 손익분기점을 구해야함

fixed, unit, price = map(int, input().split())
unit_margin = price-unit
if price <= unit: # PC가격보다 개당 생산가격이 같거나 더 비싸다면 절대 이익이 날 수 없음
    print(-1)
else:
    print(fixed // unit_margin+1) # 고정 비용을 단위 이익으로 나눈 몫에 1을 더하면 손익분기점
