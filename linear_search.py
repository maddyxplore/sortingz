# linear search 
lst = list(map(int,input().split()))

key = int(input())

for elements in lst:
    if key == elements:
        print("Key found in index:",lst.index(key)+1)
        break
else:
    print("Key not Found..!!!")
