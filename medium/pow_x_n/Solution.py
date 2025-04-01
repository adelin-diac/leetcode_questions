class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        is_negative_power = n < 0
        n = abs(n)

        while n > 0:
            if n & 1: # is n is odd
                result *= x
            x *= x
            n //= 2

        return 1/result if is_negative_power else result


## todo: try implement using recursion
s = Solution()
print(s.myPow(2.0, 10))
print(s.myPow(2.1, 3))
print(s.myPow(2.0, -2))
