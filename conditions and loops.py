a=4512
b=9071


def sum_of_odds(a,b):
    sumodd = 0
    
    for i in  range (a,b + 1):
        if i % 2 == 1:
            sumodd += i
    return sumodd

result = sum_of_odds(a,b)

print(result)
