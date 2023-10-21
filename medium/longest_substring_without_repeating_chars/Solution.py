class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      start, current = 0, 0
      max_len = 0
      char_idx = {} # {char: idx}

      while current < len(s):
        char = s[current]
        if char in char_idx and char_idx[char] >= start:
          start = char_idx[char] + 1
        
        char_idx[char] = current

        max_len = max(max_len, current - start + 1)
        current += 1
        print("-" * 50)

      return max_len
    

# print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("bbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
