from typing import List

def removeDuplicates(nums: List[int]) -> int:

    if len(nums)<2:
        return len(nums)
    counter = 0
    j = 0
    for i in range (1,len(nums)):
        if nums[i] != nums[j]:
            j+=1
            nums[j] = nums[i]
            counter =0
        else:
            if counter==0:
                j+=1
                nums[j] = nums[i]
                counter +=1
    return j+1

nums = [0,0,1,1,1,1,2,3,3]

print(removeDuplicates(nums))  