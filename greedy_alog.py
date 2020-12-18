def coin(n):
    
    coins = [1,2,5,10,20,50,100,200,500,2000]
    
    change = []
    
    i = len(coins)-1
    
    while(i>=0):
        while(n>=coins[i]):
            n-=coins[i]
            change.append(coins[i])
        i-=1
    
    return(change)
