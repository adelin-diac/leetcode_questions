from typing import List

class Solution:
    def generate(self, numRows: int)-> List[List[int]]:
        ret = [[1]]

        for i in range(1, numRows):
            row = []
            prev_len = len(ret[i-1])
            
            for j in range(0, i+1):
                prev_right = 0
                prev_left = 0

                if (j - 1 >= 0):
                    prev_left = ret[i-1][j-1]

                if (j < prev_len):
                    prev_right = ret[i-1][j]
                
                row.append(prev_left + prev_right)
            ret.append(row)
        
        return ret


print(Solution().generate(5))