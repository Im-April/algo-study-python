'''
1부터 n까지 정수의 합은 수학식 :  n x (n + 1) / 2
이를 가우스의 덧셈이라 한다.

sum = n * (n + 1) // 2
'''

def gauss_sum(n) :
    return n * (n + 1) // 2 # 정수 나눗셈 (//)

print(gauss_sum(100))  # 1부터 100까지의 합 → 5050