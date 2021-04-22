# 알파벳 대분자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
# 모든 알파벳을 오름차순으로 정렬하여 출력한 후에, 모든 숫자를 더한 값을 출력한다.
# e.g. K1KA5CB7 -> ABCKK13

import re
S = input('Enter string: ')

alpha = re.findall(r'[A-Z]', S)
nums = list(map(int, re.findall(r'[0-9]', S)))

result = ''.join(sorted(alpha))
result += str(sum(nums))
print(result)
