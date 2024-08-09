class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        

        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) > 0 and char == pairs[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
        