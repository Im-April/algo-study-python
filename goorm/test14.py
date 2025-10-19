# 입력 받기
A, B = input().split()

# 문자열 A를 파이썬 수식처럼 계산
result_A = eval(A)
result_B = eval(B)

# 더 큰 결과 출력
if result_A > result_B:
    print(result_A)
else:
    print(result_B)
