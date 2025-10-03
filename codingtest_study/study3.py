# Greedy 알고리즘
# - 탐욕법
# - 현재 상황에서 지금 당장 좋은 것만 고르는 방법

n = 1260
count = 0

# 큰 화폐부터 차례대로 확인
coins = [500, 100, 50, 10]   # ← list라는 이름은 피하는 게 좋아요(파이썬 내장 함수와 겹침)

for coin in coins:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
