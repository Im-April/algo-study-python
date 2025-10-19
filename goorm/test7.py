N = int(input())                                 # 지원자 수 입력
score = list(map(int, input().split()))          # 각 지원자의 점수 입력

# (점수, 지원자번호) 형태의 튜플 리스트 만들기
indexed_scores = [(score[i], i + 1) for i in range(N)]

# 점수를 기준으로 내림차순 정렬
indexed_scores.sort(reverse=True, key=lambda x: x[0])

# 상위 3명의 지원자 번호만 추출
top3 = [idx for s, idx in indexed_scores[:3]]

# 결과를 공백으로 구분하여 출력
print(*top3)
