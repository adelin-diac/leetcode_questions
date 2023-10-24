from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m + n > 0: 
            for i in range(len(nums2)): # O(n)
                nums1[i + m] = nums2[i]

        nums1.sort() # O((n+m)* log(n+m))
            
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:    
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        ptr = m + n - 1

        while p1 >= 0 and p2 >= 0:
          if nums1[p1] > nums2[p2]:
              nums1[ptr] = nums1[p1]
              p1 -= 1
          else:
              nums1[ptr] = nums2[p2]
              p2 -= 1
          ptr -= 1

        while p2 >= 0:
            nums1[ptr] = nums2[p2]
            p2 -= 1
            ptr -= 1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
Solution().merge(nums1, 3, nums2, 3) # [1, 2, 2, 3, 5, 6]
print(nums1)
nums1 = [1,2,3,0,0,0]
Solution().merge2(nums1, 3, nums2, 3) # [1, 2, 2, 3, 5, 6]

print(nums1)

nums1 = [1]
nums2 = []
Solution().merge(nums1, 1, nums2, 0) # [1]
print(nums1)
nums1 = [1]
Solution().merge2(nums1, 1, nums2, 0) # [1]
print(nums1)

nums1 = [0]
nums2 = [1]
Solution().merge(nums1, 0, nums2, 1) # [1]
print(nums1)
nums1 = [0]
Solution().merge2(nums1, 0, nums2, 1) # [1]
print(nums1)
