# quick_sort algorithm

def quick_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        pivot = lst.pop()
        
    lesser,greater = [],[]
    
    for item in lst:
        if item<pivot:
            lesser.append(item)
        else:
            greater.append(item)
    
    return (quick_sort(lesser) + [pivot] + quick_sort(greater))
    
print(*quick_sort([1,5,10,98,0,76,56,4,3,2,8]))
