# insertion sort 

def insertion_sort(list):

    for i in range(1,len(list)):
        cv = list[i]
        ci = i-1
        
        while (ci>=0) and cv < list[ci]:
            list[ci+1] = list[ci]
            ci-=1
        list[ci+1] = cv
    return list

print(insertion_sort([1,9,8,7,6,5,4,2,0]))
