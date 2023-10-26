class Solution:
    def kthGrammar2(self, n: int, k: int) -> int:
        hash_map = {"0": "01", "1": "10"}
        prev_item = "0"
        for i in range(1, n + 1):
            new_item = ""
            for char in prev_item:
                new_item += hash_map[char]
            prev_item = new_item
        return int(new_item[k-1])
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        row_len = 2**(n-1)
        if k <= row_len // 2:
            val = Solution().kthGrammar(n-1, k)
            return val
        else:
            val = 1 - Solution().kthGrammar(n-1, k - row_len // 2)
            return val
"""
1: 0
2: 01 
3: 0110 
4: 0110 1001 
5: 0110 1001 1001 0110
6: 0110 1001 1001 0110 1001 0110 0110 1001
7: 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110
"""

# print(Solution().kthGrammar(1, 1))
print(Solution().kthGrammar(n=2, k=1))
# print(Solution().kthGrammar(2, 2))
# print(Solution().kthGrammar(4, 3))
# print(Solution().kthGrammar(10, 100))
        