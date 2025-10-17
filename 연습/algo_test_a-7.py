# N개의 정수와 M개의 질문이 주어집니다. 각 질문은 `L R` 형태로, 
# L번째부터 R번째까지의 합을 구하세요.

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적 합 배열 생성
prefix = [0]  # prefix[0] = 0 (인덱스 계산 편의)
for num in arr:
    prefix.append(prefix[-1] + num)

# 쿼리 처리
for _ in range(m):
    l, r = map(int, input().split())
    # prefix는 1-indexed이므로 그대로 사용
    result = prefix[r] - prefix[l - 1]
    print(result)