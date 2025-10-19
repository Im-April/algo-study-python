N = int(input())
scores = list(map(int, input().split()))

max_score = 0

# 방법 1: 각 문제를 단독으로 풀었을 때
for i in range(N) :
    max_score = max(max_score, scores[i])

# 방법 2: 연속된 문제들을 풀되, 점수가 1씩 증가하는 경우
for start in range(N):
    current_sum = scores[start]
    max_score = max(max_score, current_sum)

    for end in range(start + 1, N):
        if scores[end] == scores[end - 1] + 1:
            current_sum += scores[end]
            max_score = max(max_score, current_sum)
        else:
            break

print(max_score)
