class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        first = needle[0]

        try:
          idx = haystack.index(first)
        except ValueError:
           idx = -1
        ndl_len = len(needle)

        if idx == -1:
            return idx
        
        while idx != -1:
          if needle == haystack[idx:idx+ndl_len]:
            return idx
          else:
            try: 
              idx = haystack[idx+1:].index(first) + idx + 1
              print(idx)
            except ValueError:
               idx = -1
        return -1

print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("leetcode", "leeto"))
print(Solution().strStr("hello", "ll"))
print(Solution().strStr("aaaaa", "bba"))
print(Solution().strStr("mississippi", "issip"))
