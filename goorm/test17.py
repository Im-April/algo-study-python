N = int(input())
arr = []

for _ in range(N) :
    w, v = map(int,input().split())
    arr.append((w,v)) # 튜플로 저장

best_index = 0
best_density = arr[0][0] / arr[0][1]  # 첫 번째 물질의 밀도
best_weight = arr[0][0]

for i in range(1, N):
    w, v = arr[i]
    d = w / v  # 밀도 계산

    # 조건 비교 (밀도 > 무게 > 번호 순)
    if d > best_density:
        best_density, best_weight, best_index = d, w, i
    elif d == best_density:
        if w > best_weight:
            best_density, best_weight, best_index = d, w, i
        elif w == best_weight and i < best_index:
            best_index = i

print(best_index + 1)  # 번호는 1부터 시작
    