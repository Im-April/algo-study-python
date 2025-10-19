N = int(input())
nums = list(map(int, input().split()))

total = sum(int(oct(i)[2:], 8) for i in nums)

print(oct(total)[2:])