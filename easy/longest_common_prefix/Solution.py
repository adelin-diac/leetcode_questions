from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
      return ""
    common_prefix = ""
    for letter in strs[0]:
      common_prefix += letter
      if all(word.startswith(common_prefix) for word in strs):
        continue
      else:
        return common_prefix[:-1]
    

    return common_prefix
  
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["c", "acc", "ccc"]))