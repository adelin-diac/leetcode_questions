from typing import List

class Solution:
    def remHashtagAndChar(self, st: str) -> List[str]:
        back_spc = '#'
        st_out = []
        if not back_spc in st:
            return list(st)
        for char in st:
            if(char == back_spc):
                if st_out: st_out.pop()
            else:
                st_out.append(char)
        return st_out

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_lst = Solution().remHashtagAndChar(s)
        t_lst = Solution().remHashtagAndChar(t)
        return s_lst == t_lst



s = "ab#c"
t = "ad#c"
print(Solution().backspaceCompare(s, t))

s = "ab##"
t = "c#d#"
print(Solution().backspaceCompare(s, t))

s = "a##c"
t = "#a#c"
print(Solution().backspaceCompare(s, t))

s = 'a#c'
t = 'b'
print(Solution().backspaceCompare(s, t))
