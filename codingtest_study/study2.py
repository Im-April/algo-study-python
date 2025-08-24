from random import randint
import time

# 배열에 10000개 정수 삽입
original_array = []
for _ in range(10000):
    original_array.append(randint(1, 100))

# 선택 정렬 성능 측정
array1 = original_array.copy()  # 원본 배열 복사
start_time = time.time()

# 선택 정렬 구현
for i in range(len(array1)):
    min_index = i
    for j in range(i+1, len(array1)):
        if array1[min_index] > array1[j]:
            min_index = j
    array1[i], array1[min_index] = array1[min_index], array1[i]  # 수정됨

end_time = time.time()
print(f'선택 정렬 성능 측정 : {end_time - start_time:.6f}초')

# 기본 정렬 라이브러리 성능 측정
array2 = original_array.copy()  # 원본 배열 복사
start_time = time.time()

array2.sort()

end_time = time.time()
print(f'기본 정렬 라이브러리 성능 측정 : {end_time - start_time:.6f}초')