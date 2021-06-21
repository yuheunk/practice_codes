n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
indiv = 0
for time in p:
    indiv += time
    result += indiv

print(result)