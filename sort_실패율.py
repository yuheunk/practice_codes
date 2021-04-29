# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(n, stages):
    '''
    스테이지 개수 n
    사용자가 머물러 있는 스테이지 리스트 stages

    각 스테이지를 실패율 내림차순으로 출력한다
    '''

    count = [0]*(n+1)  # 스테이지 + 1개만큼 count를 한다
    for s in range(len(stages)):
        count[stages[s]-1] += 1  # 인덱스 0은 스테이지 1과 동일하다

    failure = [[] for _ in range(len(count))]
    for i in range(len(count)):
        if sum(count[i:]) == 0:  # 만약 스테이지에 도달한 사람이 없다면
            failure[i] = [i, 0]  # 실패율은 0
        else:
            failure[i] = [i, count[i]/sum(count[i:])]  # 실패율 계산

    failure.sort(key=lambda x: (-x[1], x[0]))  # 실패율 내림차순, 스테이지 번호 오름차순
    answer = [ins[0]+1 for ins in failure if ins[0]+1 <= n]  # n+1 스테이지 번호는 제외하고 출력
    
    return answer
