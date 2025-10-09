# n 배열의 크기
# m 숫자가 더해지는 횟수
# k번 초과하면 안됨

n, m, k = map(int, input().split())
list_num = list(map(int, input().split()))

# 오름차순
list_num.sort()

first = list_num[-1]
second = list_num[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1

print(result)