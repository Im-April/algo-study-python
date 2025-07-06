# 1부터 n까지 정수의 합 구하기 2

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n 값을 입력하세요 : '))

sum = 0
for i in range(1,n+1) : # range(a,b) = a 이상 b 미만인 수를 차례로 나열하는 수열
    sum += i # i = i + 1

print(f'1부터 {n}까지 정수의 합은 {sum} 입니다.')