def primes():
    n = 1
    while True:
        n +=1
        d = 0
        for k in range(n):
            if n%(k+1) == 0:
                d+=1
        if d==2:
            d = 0
            yield n
        d = 0
k = 0        
for x in primes():
    print(x)
    k+= 1
    if k > 10:
        break
    
