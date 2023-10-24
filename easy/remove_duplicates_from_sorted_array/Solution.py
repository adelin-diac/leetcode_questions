from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev_ptr = 0
        
        for i in range(1, len(nums)):
            if(nums[i] != nums[prev_ptr]):
                prev_ptr += 1
                nums[prev_ptr] = nums[i]
            i += 1
        return prev_ptr + 1

# print(Solution().removeDuplicates([1,1,2]))
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
print(nums)

nums = [1,1]
print(Solution().removeDuplicates(nums))
print(nums)

nums = [1,2]
print(Solution().removeDuplicates(nums))
print(nums)
