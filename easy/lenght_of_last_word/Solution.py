class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.strip().split(" ")[-1]
        return len(last)


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))