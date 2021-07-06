import re
def solution(dartResult):
    dart_lst = re.findall(r'\d{1,2}\w{1}[^A-Z0-9]*', dartResult)

    answer = []
    for d in dart_lst:
        num = int(re.findall(r'\d+', d)[0])
        alp = re.findall(r'[A-Z]', d)[0]
        sym_lst = re.findall(r'[#*]', d)

        if alp == 'T':
            num = num ** 3
        elif alp == 'D':
            num = num ** 2
        
        if sym_lst != []:
            sym = sym_lst[0]
            if sym == '*':
                num *= 2
                if len(answer)>=1:
                    answer[-1] *= 2
            elif sym == '#':
                num *= (-1) 
        
        answer.append(num)
    return sum(answer)