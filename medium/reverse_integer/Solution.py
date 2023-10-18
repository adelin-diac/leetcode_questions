class Solution:
  def reverse(self, x: int) -> int:
    # first bit is sign bit
    MIN = -2**31
    MAX = 2**31

    x_str = str(x)

    x_str = x_str[::-1]

    if x_str.endswith("-"):
      x_str = "-" + x_str[:-1]

    num = int(x_str)
    if num not in range(MIN, MAX):
      return 0

    return x_str
  
  def reverse2(self, x: int) -> int:
    MAX = 2**31 - 1

    ans = 0
    is_neg = x < 0

    x = abs(x)

    while x:
      ans = ans * 10 + x % 10
      x = x // 10

    if ans > MAX:
      return 0
    return -ans if is_neg else ans    


print(Solution().reverse2(123))
print(Solution().reverse2(-123))
