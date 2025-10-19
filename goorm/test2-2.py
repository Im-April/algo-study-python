N = input()
S = input()
result = ''

for i in S :
    if i == i.upper() :
        result += i.lower()
    elif i == i.lower() :
        result += i.upper()

print(result)

