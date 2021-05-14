n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, len(array)):
    for j in range(len(array[i])):
        if j == 0:
            array[i][j] += array[i-1][j]
        elif j == len(array[i])-1:
            array[i][j] += array[i-1][j-1]
        else:
            array[i][j] += max(array[i-1][j], array[i-1][j-1])

print(max(array[-1]))
