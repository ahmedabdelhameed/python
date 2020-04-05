from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        item_count = len(nums)
        nums_map =  {}
        
        final =[]
       
        for i in range(0,len(nums)):
            complement = target - nums[i] 
            if nums_map  and nums_map.__contains__(complement):
                final.append(nums_map[complement])
                final.append(i)
               
                return final
            else:
                nums_map[nums[i]] = i
        return final       

nums = [2, 7, 11, 15]
target = 9


print(twoSum(nums,target))  