n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]

values.sort(reverse=True)
count = 0
for v in values:
    count += k//v
    k %= v

print(count)