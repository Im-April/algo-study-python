N,M = map(int,input().split())
arr_n = list(map(int,input().split()))
arr_m = []

for i in arr_n :
	if i % M == 0 :
		arr_m.append(i)
	else :
		arr_m.append(i*M)


print(*arr_m)