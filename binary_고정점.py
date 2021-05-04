n = int(input())
array = list(map(int, input().split()))

def fixed_pnt(array, start, end):
    if start > end:
        return None

    mid = (start+end)//2
    if array[mid] == mid:
        return mid
    elif array[mid]>mid:
        return fixed_pnt(array, start, mid-1)
    else:
        return fixed_pnt(array, mid+1, end)

result = fixed_pnt(array, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)
