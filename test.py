def rabbit_pairs(n, k):
    # Base cases: in month 1 and 2, there is exactly 1 rabbit pair.
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    # Initialize the number of rabbit pairs for the first two months
    prev2, prev1 = 1, 1
    
    # Calculate the number of rabbit pairs for each month from 3 to n
    for month in range(3, n + 1):
        current = prev1 + k * prev2
        prev2, prev1 = prev1, current
    
    return prev1

# Example input: n = 5, k = 3
n = 5  # Number of months
k = 3  # Number of rabbit pairs produced by each reproductive pair

# Output the total number of rabbit pairs after n months
result = rabbit_pairs(n, k)
print(result)
