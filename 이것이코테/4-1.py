n = int(input())        # 격자판 크기
x, y = 1, 1            # 시작 좌표 (1,1)
plans = input().split() # 이동 명령어들 ['L', 'R', 'U', 'D']

# 방향 벡터 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans: # ['R', 'R', 'D', 'U']를 하나씩
    # 이동 후 좌표 계산
    for i in range(len(move)): # 0, 1, 2, 3
        if plan == move[i]:
            nx = x + dx[i] # 새로운 x 좌표
            ny = y + dy[i] # 새로운 y 좌표
            # 공간을 벗어나는 경우 무시
            if nx < 1 or ny < 1 or nx > n or ny > n:
                break   # 범위 벗어나면 이 명령 무시하고 다음 plan으로
            # 이동 수행
            x, y = nx, ny
            break  # 일치하는 move 찾았으니 반복 종료

print(x, y)
