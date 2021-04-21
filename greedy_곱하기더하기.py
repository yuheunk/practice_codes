# 각 자리가 숫자(0-9)로만 이루어진 문자열 S가 주어졌을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 'x' 또는 '+' 연산자를 넣어
# 가장 큰 수를 구하는 프로그램을 작성하시오.
# 단, 'x'가 '+'보다 먼저 계산되지 않고 모든 연산은 왼쪽에서부터 순서대로 이루어진다.
# e.g. '02984' -> 0+2 x 9 x 8 x 4 = 576

string = input('Enter string of numbers: ')
nums = list(map(int, string))

result = nums[0]
for num in nums[1:]:
    if num == 0 or num==1:
        result += num
    elif result==0 or result==1:
        result += num
    else:
        result *= num
        
print(result)
