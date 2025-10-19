from collections import deque

# 입력
N, K = map(int, input().split())
q = deque()  # 큐 생성

for _ in range(N):
    cmd = input().split()  # 명령 입력
    if cmd[0] == "push":
        x = int(cmd[1])
        if len(q) == K:  # 큐가 가득 찬 경우
            print("Overflow")
        else:
            q.append(x)
    elif cmd[0] == "pop":
        if not q:  # 큐가 비어 있는 경우
            print("Underflow")
        else:
            print(q.popleft())
