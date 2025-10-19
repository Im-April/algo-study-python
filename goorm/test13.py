import sys

# 입력
N = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 0의 위치 찾기
zr = zc = -1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0:
            zr, zc = i, j
            break
    if zr != -1:
        break

# 같은 행과 같은 열의 합 계산
row_sum = sum(grid[zr])
col_sum = sum(grid[i][zc] for i in range(N))

# 0은 두 번 더해져도 값에 영향 없음
answer = row_sum + col_sum

print(answer)
