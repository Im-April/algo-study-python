# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요 ? : '))

for i in range(n) :
    '''
    if i % 2:        # 이것도 OK (파이썬에서는 True로 간주됨)
    if i % 2 == 1:   # 이게 더 **명시적**이고 이해하기 쉬움
    '''
    if i % 2 :
        print('-', end='') # 홀수인 경우 - 출력
    else :
        print('+', end='') # 짝수인 경우 + 출력

print()