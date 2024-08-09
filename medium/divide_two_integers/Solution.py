class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = 0
        positive = True

        dvdn = abs(dividend)
        d = abs(divisor)

        if (dividend < 0) ^ (divisor < 0):
            positive = False

        if dvdn == d:
            return 1 if positive else -1
        
        if d > dvdn or dvdn == 0:
            return 0
        
        if d == 1:
            ret = dvdn
            if not positive:
                ret = -ret
            return min(max(-2**31, ret), 2**31 - 1)
        
        while dvdn >= d:
            temp = d
            multiple = 1

            while dvdn >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dvdn -= temp
            ret += multiple
        
        if not positive:
            ret = -ret

        return min(max(-2**31, ret), 2**31 - 1)
            
        