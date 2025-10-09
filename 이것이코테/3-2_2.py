n, m, k = map(int, input().split())
list_num = list(map(int, input().split()))

# 오름차순
list_num.sort()

first = list_num[-1]
second = list_num[-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 두번째로 큰 수 더하기

print(result) # 최종 답안