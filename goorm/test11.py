N = int(input())
arr = [[0]*N for _ in range(N)]

num = 1

for i in range(N) :
    for j in range(N) :
        arr[i][j] = num
        num += 1

for row in arr :
    print(*row)