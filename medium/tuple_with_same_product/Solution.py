from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        len_nums = len(nums)

        results = defaultdict(list)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                product = nums[i] * nums[j]
                results[product].append((nums[i], nums[j]))
                
        ret = 0
        for unique_pairs in results.values():
            l = len(unique_pairs)
            print(unique_pairs)
            if l > 1:
                ret += l * (l-1) * 4

        return ret



s = Solution()

print(s.tupleSameProduct([2,3,4,6]))
print(s.tupleSameProduct([1,2,4,5,10]))
print(s.tupleSameProduct([2,3,4,6,8,12]))