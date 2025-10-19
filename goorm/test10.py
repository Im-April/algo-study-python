N, M = map(int, input().split())
cards = [int(input()) for _ in range(M)]

collected = set()  # 지금까지 모은 카드 종류
answer = -1        # 기본값 (-1: 못 모은 경우)

for i in range(M):
    collected.add(cards[i])  # 카드 추가
    if len(collected) == N:  # 모든 종류를 다 모은 순간
        answer = i + 1       # 현재까지 받은 카드 개수
        break

print(answer)

	