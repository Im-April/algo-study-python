# 1부터 n까지 정수의 합 구하기 2

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('몇 개를 출력할까요? : '))

for _ in range(n//2) : # _는 변수를 쓰지 않을 때 관습적으로 사용하는 이름
    print('+-', end='')


if n % 2 :
    print('+', end='')

print()