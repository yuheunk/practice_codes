def solution(s):
    result = 10000

    for i in range(1, len(s)//2+2):
        start = s[:i]
        cnt = 1
        answer = ''
        
        for j in range(i, len(s), i):
            next = s[j:j+i]
            if start == next:
                cnt += 1
            else:
                if cnt < 2:
                    answer += start
                else:
                    value = str(cnt)+start
                    answer += value
                cnt = 1
                start = next
        if cnt < 2:
            answer += start
        else:
            value = str(cnt)+start
            answer += value

        result = min(len(answer), result)
    return result
