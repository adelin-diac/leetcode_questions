from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ret = []
        # right, down, left, up
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        num_steps = 1 # increases every 2
        
        row = rStart
        col = cStart

        while rows * cols > len(ret):
            for _ in range(2):
                for _ in range(num_steps):

                    # if within bounds, add to ret
                    if 0 <= row < rows and 0 <= col < cols:
                        ret.append([row, col])

                    row = row + direction[d][0]
                    col = col + direction[d][1]

                d = (d + 1) % 4

            num_steps = num_steps + 1
        
        return ret


