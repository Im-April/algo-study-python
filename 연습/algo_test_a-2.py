# 🧩 예제 2. 최댓값과 인덱스 구하기

# 문제:
# 9개의 자연수가 주어질 때, 최댓값과 그 위치(인덱스)를 출력하시오.

nums = [int(input()) for _ in range(9)]
max_value = max(nums)
print(max_value)
print(nums.index(max_value) + 1)


