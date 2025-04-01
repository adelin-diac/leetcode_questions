from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
      
        if not nums:
            return 0

        sum = nums[0]
        largest = nums[0]
        for idx in range(1,len(nums)):
            if nums[idx] > nums[idx-1]:
                sum += nums[idx]
                if sum > largest:
                    largest = sum
            else:
                sum = nums[idx]
        return largest
    

s = Solution()
print(s.maxAscendingSum([10,20,30,5,10,50]))
print(s.maxAscendingSum([10,20,30,40,50]))
print(s.maxAscendingSum([12,17,15,13,10,11,12]))