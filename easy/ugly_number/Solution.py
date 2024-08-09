class Solution:
    def isUgly(self, n: int) -> bool:
        ugly_primes = [2,3,5]

        while n/2 % 1 == 0:
            n /= 2
        
        while n/3 % 1 == 0:
            n /= 3

        while n/5 % 1 == 0:
            n /= 5

        return False if n > 1 else True

        


s = Solution()
print(s.isUgly(49))