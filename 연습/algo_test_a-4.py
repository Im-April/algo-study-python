# N개의 정수가 주어질 때, 배열을 왼쪽으로 K번 회전시킨 결과를 출력하세요.

n,k = map(int, input().split())
arr = list(map(int, input().split()))

# 불필요한 반복을 줄일 수 있다.
k = k % n

# 왼쪽으로 k번 회전
result = arr[k:] + arr[:k]

print(' '.join(map(str, result)))