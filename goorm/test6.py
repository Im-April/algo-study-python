N, K = input().split()
nums = input().split()

result = []

for i in nums:
    if K not in i: # K가 포함되지 않은 숫자만 추가
        result.append(i)

print(len(result))