# (1, 1) 에서 (n, m)까지 m번을 걸쳐
# 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
# 테스트 케이스마다 채굴자가 얻을 수 있는 최대 금의 크기를 출력

t = int(input())  # num of test case
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    array = [array[m*i:m*(i+1)] for i in range(n)]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                array[j][i] += max(array[j][i-1], array[j+1][i-1])
            elif j == n-1:
                array[j][i] += max(array[j-1][i-1], array[j][i-1])
            else:
                array[j][i] += max(array[j-1][i-1], array[j][i-1], array[j+1][i-1])
    
    print(max([array[_][-1] for _ in range(len(array))]), end='\n')
