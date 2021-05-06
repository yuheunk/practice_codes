# 일직선상에 여러 채의 집이 위치함.
# 이 중 하나에 안테나를 설치하는데 모든 집까지의 거리가 최소가 되도록 설치한다.
# output: 설치할 집의 위치(여러 개면 가장 작은 값)

n = int(input('number of houses'))
houses = list(map(int, input('Location of houses').split()))

houses.sort()
if len(houses)%2==0:
    print(houses[len(houses)//2-1])
else:
    print(houses[len(houses)//2])
