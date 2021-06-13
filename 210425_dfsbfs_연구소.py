#%%
# 지도의 세로 N, 가로 M이 주어진다.
# 0: 빈칸, 1: 벽, 2: 바이러스
# 새로 세울 수 있는 벽은 3개일 때, 세우고 바이러스가 퍼진 뒤 안전구역의 최댓값을 구한다.

n, m = map(int, input('가로, 세로: ').split())

virus_map = []
for _ in range(n):
    virus_map.append(list(map(int, input('virus map:').split())))

# 2랑 연결되어 있는 0을 다 찾는다.(상하좌우) DFS
# 2와 근접한 0값에 임의로 1을 세개 넣고 그 사이의 0의 개수를 계산한다.
# 최대 0의 개수를 도출한다.
#%%
def virus_pth():
    pass