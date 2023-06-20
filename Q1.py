# Q1
# We have N glasses with capacity 1, 2, ..., N liters. The glasses are initially empty.
# We have total K liters of water.
# What is the minimum number of glasses that we need to contain K liters of water?    
# Pouring water from an already filled glass is not allowed
# If it is not possible to contain K liters of water, return -1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, K):
    # Implement your solution here
    if K <= N:
        return 1
    
    if N*(N+1)/2 < K:
        return -1
    
    result = 0

    while K > 0:
        if K >= N:
            K -= N
            N -= 1
            result += 1
        else: 
            result += 1
            break
    
    return result
