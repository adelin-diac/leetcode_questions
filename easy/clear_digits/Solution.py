class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        for char in s:
            if char.isdigit():
                if result: result.pop()
            else:
                result.append(char)
        return ''.join(result)

"""
initial implementaion with string concatenation was not memory efficient
because string concatenation creates a new string.

The same with string slicing.

A list is a better method of doing it
"""

s = Solution()
print(s.clearDigits("cb34"))
print(s.clearDigits("abc"))
print(s.clearDigits("abc2"))

