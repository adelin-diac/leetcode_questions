from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        prev_ptr = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[prev_ptr] = nums[i]
                prev_ptr += 1
        return prev_ptr


nums = [3,2,2,3]
print(Solution().removeElement(nums, 3))
print(nums)

nums = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(nums, 2))
print(nums)

nums = [2]
print(Solution().removeElement(nums, 3))
print(nums)

nums = [1]
print(Solution().removeElement(nums, 1))
print(nums)