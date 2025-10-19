N = int(input())
event_time = []

for _ in range(N):
    s, e = map(int, input().split())
    event_time.append((s, e))

# 종료 시간 기준으로 정렬
event_time.sort(key=lambda x: x[1])

count = 0
end_time = -1  # 마지막으로 선택한 행사의 종료 시각

# 각 행사 (s, e)에 대해 검사
for s, e in event_time:
    if s >= end_time + 1:
        count += 1
        end_time = e  # 현재 행사의 종료 시각 갱신

print(count)
