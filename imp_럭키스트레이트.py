# 점수 N(무조건 짝수개의 숫자로 이루어짐)을 반으로 나누어서
# 왼쪽 반과 오른쪽 반의 숫자의 합이 같으면 LUCKY, 아니면 READY

N = int(input('Input score(even number of numbers): '))

str_N = str(N)
middle = len(str_N)//2
first = list(map(int, str_N[:middle]))
second = list(map(int, str_N[middle:]))

if sum(first) == sum(second):
    print('LUCKY')
else:
    print('READY')
