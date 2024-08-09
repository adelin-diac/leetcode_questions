from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []

        for i in range(len(intervals) - 1):
            print(i)

        return ret
    

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))