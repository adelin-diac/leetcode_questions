from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_ltrs = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        result = []
        def combine(combination, next_digits):
            if next_digits == "":
                result.append(combination)
            else:
                for letter in num_ltrs[next_digits[0]]:
                     combine(combination + letter, next_digits[1:])
            return result
        combination = combine("", digits)

        return combination


print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("2"))
print(Solution().letterCombinations("8723"))