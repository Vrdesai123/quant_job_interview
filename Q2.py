### Switching array problem
# We call an array swtiching if all numbers in even positions are equal and all numbers in odd positions are equal.
# Given an array A of integers, we want to find the length of the longest switching subarray of A.  

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    if len(A) <= 2:
        return len(A)
    
    final_best = 2
    best = 2
    
    for i in range(2, len(A)):
        if A[i] == A[i-2]:
            best += 1
        else:
            best = 2
        final_best = max(final_best, best)
    return final_best
            





   
            