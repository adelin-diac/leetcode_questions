from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        ret = []
        for item in strs:
            item_sorted = ''.join(sorted(item))

            if item_sorted in grouped:
              grouped[item_sorted].append(item)
            else:
                grouped[item_sorted] = [item]
        
        for key in grouped:
            ret.append(grouped[key])

        return ret


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
print(s.groupAnagrams([]))