def merge(left,right):
    res = []
    i,j = 0,0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res += left[i:]
    res += right[j:]
    return res

def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)

lst = list(map(int, input().split()))
print(mergesort(lst))
