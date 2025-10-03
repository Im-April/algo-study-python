# n : 숫자의 개수
# m : 총 더할 횟수
# k : 같은 수를 연속해서 더할 수 있는 최대 횟수

# n,m,k를 공백으로 구분하여 입력
n,m,k = map(int, input().split())
 
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 수 정렬
first = data[n-1]
second = data[n-2] 

result = 0

while True :
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1 

print(result)
