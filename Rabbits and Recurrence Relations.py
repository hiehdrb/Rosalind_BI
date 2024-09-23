
n=29
k=2

def rabbit_pairs(n, k):
    if n ==1:
        return 1
    elif n==2:
        return 1

    prev2, prev1 = 1, 1


    for month in range (3, n + 1):
        current = prev1 + k*prev2
        prev2, prev1 = prev1, current

    return prev1

result = rabbit_pairs(n,k)


print(result)
    
