class Solution:
    def romanToInt(self, s: str) -> int:
        vals_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for idx, val in enumerate(s):
            int_val = vals_map[val]
            if(idx + 1 < len(s)):
              next_val = s[idx+1]
              if(int_val < vals_map[next_val]):
                  int_val = - int_val
               
            res += int_val
        return res

print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
