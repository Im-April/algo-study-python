# 입력받은 정수의 부호 (양수,음수,0) 출력하기

n = int(input('정수를 입력하세요. : '))

if n > 0 :
    print(f'{n}은 양수 입니다.')
elif n < 0 :
    print(f'{n}은 음수 입니다.')
else :
    print(f'{n}은 0 입니다.')