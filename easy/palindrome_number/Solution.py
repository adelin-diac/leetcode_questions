# CAN IMPROVE BY DOING WITHOUT CONVERTING TO STRING

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0): return False
        else:
            x = str(x)
            for i in range(0, len(x)):
                if x[i] == x[len(x)-1-i]:
                    continue
                else:
                    return False
            return True
# --------------- OR ---------------- #
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if(x<0): return False
#         else:
#             x = str(x)
#             rev = x[::-1]
#             if x==rev:
#                 return True
#             else:
#                 return False

s = Solution()