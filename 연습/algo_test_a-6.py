# N×M 크기의 배열을 1부터 순서대로 채우되, 지그재그 패턴으로 채우세요.

n,m = map(int,input().split())

# 2차원 배열 생성
arr = [[0] * m for _ in range(n)] # n개의 행, 각 행에 m개의 0을 넣은 2차원 리스트
num = 1

for i in range(n):
    if i % 2 == 0:
        # 짝수행 : 왼쪽에서 오른쪽
        for j in range(m):
            arr[i][j] = num
            num += 1

    else :
        # 홀수행 : 오른쪽에서 왼쪽
        for j in range(m-1,-1,-1): # range(start, stop, step)
            arr[i][j] = num
            num += 1

for row in arr :
    print(' '.join(map(str, row)))
