# n: 도시 수 / m: 도로 수 / k: 최단거리 / x: 시작점
# (A, B): A에서 B로 가는 단방향 도로가 존재한다.
# 출력: 시작점에서 최단거리가 k인 도시들을 오름차순으로 한줄에 뽑는다.
# 하나도 존재하지 않으면 -1 출력

from collections import deque
n, m, k, x = map(int, input('n, m, k, x: ').split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input('single directed graphs: ').split())
    graph[start].append(end)

def city_distance(start_pnt, num_city, short_pth):
    distance = [0]*(num_city+1)
    que = deque([start_pnt])

    while que:
        start = que.popleft()
        for next in graph[start]:
            if distance[next] == 0:
                distance[next] = distance[start] + 1
                que.append(next)
    
    result = False
    for i in range(len(distance)):
        if distance[i] == short_pth:
            print(i)
            result = True
    if result == False:
        print(-1)

city_distance(x, n, k)
