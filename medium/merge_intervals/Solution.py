from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0]) # O(n*log(n))
        ret = []
        
        for interval in intervals:
          if ret and interval[0] <= ret[-1][1]:
             # merge intervals (check for the max end time in
             # case previous interval fully covers the next one)
             ret[-1] = [ret[-1][0], max(interval[1], ret[-1][1])]
          else: ret.append(interval)

        return ret
    
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[4,5], [1,4]]))
print(Solution().merge([[1,4],[2,3]]))
print(Solution().merge([[1,4],[0,2],[3,5]]))