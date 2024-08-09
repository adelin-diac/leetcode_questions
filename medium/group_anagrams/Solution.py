class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for item in strs:
            grouped[item.sort()].append(item)
        
        return grouped