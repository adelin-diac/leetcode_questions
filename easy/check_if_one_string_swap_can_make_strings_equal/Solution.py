class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if not len_s1 == len_s2 :
            return False
        
        if s1 == s2:
            return True
        
        ## UNOPTIMAL
        # for i in range(len_s2):
        #     for j in range(i, len_s2):
        #         word = list(s2)
        #         word[i], word[j] = s2[j], s2[i]

        #         if s1 == ''.join(word):
        #             return True
        mismatches = []
        for i in range(len_s1):
            if not s1[i] == s2[i]:
                mismatches.append(i)

        if len(mismatches) == 2:
            return s1[mismatches[0]] == s2[mismatches[1]] and s1[mismatches[1]] == s2[mismatches[0]]
        
        return False
    

s = Solution()
print(s.areAlmostEqual("bank", "kanb"))
print(s.areAlmostEqual("attack", "defend"))
print(s.areAlmostEqual("kelb", "kelb"))
