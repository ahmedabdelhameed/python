#Given an array A of integers, return true if and only if it is a valid mountain array.

#Recall that A is a mountain array if and only if:

    #A.length >= 3
    #There exists some i with 0 < i < A.length - 1 such that:
        #A[0] < A[1] < ... A[i-1] < A[i]
        #A[i] > A[i+1] > ... > A[A.length - 1]

from typing import List
def validMountainArray(A: List[int]) -> bool:
    
    if len(A)<3:
        return False
    i = 0
    while i+1< len(A) and (A[i] < A[i+1]):
        i+=1
        
    if i==0 or i == (len(A)-1):
        return False
    while i+1< len(A) and (A[i] > A[i+1]):
        i+=1 
    if i == (len(A)-1):
        return True
    else:
        return False


#print(validMountainArray([8,4,3]))

print(validMountainArray([0,3,2,1])
