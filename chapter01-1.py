# 세 정수를 입력받아 최댓값 구하기

print('세 정수를 입력하세요.')
a = int(input('정수 a를 입력하세요. : '))
b = int(input('정수 b를 입력하세요. : '))
c = int(input('정수 c를 입력하세요. : '))

maximum = a
if maximum < b : maximum = b
if maximum < c : maximum = c

print(f'최댓값은 {maximum} 입니다.')