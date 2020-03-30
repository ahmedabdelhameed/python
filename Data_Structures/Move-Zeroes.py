#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Example:

#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]


from typing import List

def moveZeroes(nums: List[int]) -> None:
    j = 0
    for i in range(0, len(nums)):
      if nums[i] != 0:
        nums[j] = nums[i]
        j +=1
    for x in range (j,len(nums)):
      nums[x]=0
      

#Sample run
#mylist= [0,1,0,3,1,2]
#moveZeroes(mylist)
#print(mylist)
       
        