n, x = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
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
            return binary_search(array, target, start, mid-1)
        
        elif array[mid] > target:
            return binary_search(array, target, start, mid-1)
        else:
            return binary_search(array, target, mid+1, end)
    return -1

count = 0
result = binary_search(array, x, 0, n-1)

if result != -1:
    for a in array[result:]:
        if a==x:
            count+=1
else:
    count = -1

print(count)
