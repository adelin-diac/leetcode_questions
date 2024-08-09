from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     # O(n*log(n)) + O(n) + O(n*log(n))
        #     return True
        # else: return False
        s_counts = Counter(s) # O(n)
        t_counts = Counter(t) # O(n)

        if len(s_counts) != len(t_counts): # O(1)
            return False

        for s_ltr in s_counts: # O(n)
            if s_counts[s_ltr] != t_counts[s_ltr]:
                return False
        
        return True

print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))