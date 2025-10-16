# 🧩 1단계: 기본 자료구조 & 구현력 다지기

## 📚 핵심 개념 정리

### 1. 입력 처리 패턴

```python
# 단일 입력
n = int(input())

# 공백으로 구분된 여러 값
a, b = map(int, input().split())

# 리스트로 받기
arr = list(map(int, input().split()))

# 여러 줄 입력
data = [input() for _ in range(n)]
```

### 2. 자주 쓰는 출력 패턴

```python
# 공백으로 구분
print(*arr)  # 또는 print(' '.join(map(str, arr)))

# 줄바꿈으로 구분
print('\n'.join(map(str, arr)))

# 포맷팅
print(f"{result}")
```
