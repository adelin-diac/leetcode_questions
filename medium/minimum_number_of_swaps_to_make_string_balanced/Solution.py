class Solution:
    """
    `Link:` https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
    """
    def minSwaps(self, s:str) -> int:
        imbal = 0
        for char in s:
                
            if char == ']':
                if imbal == 0:
                    imbal += 1
                else:
                    imbal -= 1
            else:
                imbal += 1
        
        return (imbal + 1) // 2


print(Solution().minSwaps("][]["))