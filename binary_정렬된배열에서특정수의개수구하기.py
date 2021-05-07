n, x = map(int, input().split())
array = list(map(int, input().split()))

def lft_search(array, target, start, end):
    if len(array)==1:
        if target in array:
            return array.index(target)
        else:
            return -1

    while start <= end:
        mid = (start+end)//2

        if array[mid] == target and array[mid-1] < target:
            return mid
        
        elif array[mid] == target and array[mid-1] >= target:
            return lft_search(array, target, start, mid-1)
        
        elif array[mid] > target:
            return lft_search(array, target, start, mid-1)
        else:
            return lft_search(array, target, mid+1, end)
    return -1

def rgt_search(array, target, start, end):
    if len(array)==1:
        if target in array:
            return 1
        else:
            return -1

    while start <= end:
        mid = (start+end)//2

        if array[mid] == target and array[mid+1] > target:
            return mid
        
        elif array[mid] == target and array[mid+1] <= target:
            return rgt_search(array, target, mid+1, end)
        
        elif array[mid] > target:
            return rgt_search(array, target, start, mid-1)
        else:
            return rgt_search(array, target, mid+1, end)
    return -1


start = lft_search(array, x, 0, n-1)  # target 숫자가 시작하는 인덱스
end = rgt_search(array, x, 0, n-1)  # target 숫자가 끝나는 인덱스

if start != -1 and end != -1:
    print(end-start+1)
else:
    print(start)
