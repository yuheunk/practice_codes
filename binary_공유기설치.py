n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1]-array[0]
end = array[-1]-array[0]
max_dist = 0
cnt = 1

while start <= end:
    mid = (start+end)//2  # 공유기 설치한 후에 집들 사이의 거리 중 최소값
    pnt = array[0]  # 공유기 설치하는 집의 시작점
    for i in range(1, n):
        if array[i]-pnt >= mid:  # 집들 사이의 거리는 최솟값과 같거나 커야 한다
            pnt = array[i]  # 그 다음 설치한 집에서의 거리를 구해야 되니깐 포인트를 이동
            cnt+=1  # 설치된 공유기 개수를 더한다

    if cnt >= c:  # 만약 공유기 개수가 정해진 것과 같거나 크면(같은 경우는 최대값을 구하기 위해서)
        max_dist = mid
        start = mid+1
    else:  # 공유기 개수가 적으면 거리를 더 좁혀야지
        end = mid-1

print(max_dist)
