from collections import Counter
from typing import List

class Solution:
    # not optimised
    # Run complexity -> O(n*m)
    # Space complexity -> O(min(n, m)) -> 'ret' is additional space

    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     ret = []
    #     for num in nums1:
    #         if num in nums2:
    #             ret.append(num)
    #             nums2.remove(num)
    #
    #     return ret

    # Time complexity -> O(n+m)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1) # time = O(n)
        ret = [] # space = O(n)
        for num in nums2: # time = O(m)
            if num in counts1 and counts1[num] > 0:
                ret.append(num)
                counts1[num] -= 1
        
        return ret