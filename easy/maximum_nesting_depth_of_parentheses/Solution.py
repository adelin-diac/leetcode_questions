class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for char in s:
          if char == '(':
              depth += 1
              if depth > max_depth:
                max_depth = depth
          elif char == ')':
              depth -= 1

        return max_depth


print("Sol1: ", Solution().maxDepth("(1+(2*3)+((8)/4))+1"))
print("Sol2: ", Solution().maxDepth("(1)+((2))+(((3)))"))