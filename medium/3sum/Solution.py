class Solution:
    # Unoptimised solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ret = []
        # # nums = sorted(nums) # n*log(n)
        # for i in range(0, len(nums)): # n^3
        #     for j in range(1, len(nums)):
        #         if i == j:
        #             continue
        #         for k in range(2, len(nums)):
        #             if i == k or j == k:
        #                 continue
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 arr_to_append = sorted([nums[i], nums[j], nums[k]])
        #                 if not arr_to_append in ret:
        #                     ret.append(arr_to_append)

        # -4, -1, -1, 0, 1, 2
        ret = []
        nums = sorted(nums) # n * log(n)
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                
                elif total > 0:
                    right -= 1

                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ret