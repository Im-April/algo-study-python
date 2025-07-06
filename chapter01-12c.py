# 1부터 n까지 정수의 합 구하기 1 (for문 수정)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('몇 개를 출력할까요? : '))

for i in range(1,n+1) :
    if i % 2 == 1 :
        print('+', end='')
    else :
        print('-', end='')

print()