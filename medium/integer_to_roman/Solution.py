class Solution:
    def intToRoman(self, num: int) -> str:
      values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
      symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
      roman = ""
      for idx, val in enumerate(values):
         while num >= val:
            num -= val
            roman += symbols[idx]
      
      return roman
    
    def intToRoman2(self, num: int) -> str:
      values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
      symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
      roman = ""
      for idx, val in enumerate(values):
         amount = num // val
         roman += symbols[idx] * amount
         num = num % val
      
      return roman
      

print(Solution().intToRoman(3))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))

print(Solution().intToRoman2(3))
print(Solution().intToRoman2(58))
print(Solution().intToRoman2(1994))
