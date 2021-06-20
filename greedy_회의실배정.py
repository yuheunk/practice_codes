n = int(input())
times = []
for _ in range(n):
    start, end = map(int, input().split())
    times.append((start, end))
times.sort(key = lambda x: (x[1], x[0]))

count = 0
end = 0
for a, b in times:
    if a >= end:
        count += 1
        end = b
print(count)