import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        power = math.log(n, 4)
        return power % 1 == 0.0


for i in range(10):
    n = 4 ** (i + 1)
    print(n, " -- is power of four:\t", Solution().isPowerOfFour(n))

for i in range(5):
    n = 4 ** (i + 1) + 1
    print(n, " -- is power of four:\t", Solution().isPowerOfFour(n))