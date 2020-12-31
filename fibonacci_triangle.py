# fibannaci triangle 

n = 5 # int(input())

def fibannaci(n):
    l = [1,2]
    a,b = 1,2
    for i in range(2,n):
        c = a+b
        a,b = b,c
        l.append(c)
    return l

lst = fibannaci(n)

for i in range(1,n+1):
    for j in range(i):
        print(lst[j],end=" ")
    print()
