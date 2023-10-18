from collections import defaultdict
from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for idx, val in enumerate(nums):
        for idx2, val2 in enumerate(nums[idx:], start=idx):
           if idx == idx2:
              continue
           if val + val2 == target:
              return [idx, idx2]
  def twoSum_more_efficient(self, nums: List[int], target: int) -> List[int]:
     hash_map = defaultdict(int) # val: idx
     for idx, val in enumerate(nums):
        diff = target - val
        if(diff in hash_map):
           return [hash_map[diff], idx]
        else:
           hash_map[val] = idx
           


print(Solution().twoSum_more_efficient(nums=[2,7,11,15], target=9))
print(Solution().twoSum_more_efficient(nums=[3,2,4], target=6))
print(Solution().twoSum_more_efficient(nums=[3, 3], target=6))
