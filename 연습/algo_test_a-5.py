# N장의 카드에 숫자가 적혀있습니다. 카드를 M번 섞는데, 각 섞기는 다음과 같습니다:
# - `1 A B`: A번째와 B번째 카드를 교환
# - `2 A`: A번째 카드를 맨 뒤로 이동

# 모든 섞기가 끝난 후 카드 배열을 출력하세요.

n = int(input())
cards = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    command = list(map(int, input().split()))
    
    if command[0] == 1:
        # A번째와 B번째 교환 (1-indexed → 0-indexed)
        a, b = command[1] - 1, command[2] - 1
        cards[a], cards[b] = cards[b], cards[a]
    
    elif command[0] == 2:
        # A번째를 맨 뒤로
        a = command[1] - 1
        card = cards.pop(a)
        cards.append(card)

print(' '.join(map(str, cards)))
