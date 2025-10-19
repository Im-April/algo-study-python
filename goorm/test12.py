len_s, len_e = map(int, input().split())
s = input().strip()
e = input().strip()

# 대소문자 구분 없는 비교
s_lower = s.lower()  # 비교용 (소문자)
e_lower = e.lower()  # 비교용 (소문자)

while s_lower in e_lower:  # 단어가 포함되어 있으면 계속 반복
		idx = e_lower.find(s_lower)  # 처음 등장하는 위치 찾기
		# 해당 부분 삭제
		e = e[:idx] + e[idx + len(s):]
		e_lower = e_lower[:idx] + e_lower[idx + len(s):]

# 결과 출력
print(e if e else "EMPTY")