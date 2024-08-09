from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # O(n*log(n))
        val = nums[0] + nums[1] + nums[2]

        for i in range(0, len(nums) - 1):
          left, right = i+1, len(nums) - 1

          # sorted array, update left and right ptr accordingly to
          # either increase or decrease the sum
          while left < right: 
            new_val = nums[i] + nums[left] + nums[right]

            # check if we are closer to the target
            if abs(target - new_val) < abs(target - val):
                val = new_val

            # update pointers accordingly
            if new_val < target:
               left += 1
            elif new_val > target:
               right -=1
            elif new_val == target:
               break

        return val

s = Solution()
print(s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
print(s.threeSumClosest([-1,2,1,-4], 1))
print(s.threeSumClosest([0, 0, 0], 1))
print(s.threeSumClosest([1,1,1,0], -100))