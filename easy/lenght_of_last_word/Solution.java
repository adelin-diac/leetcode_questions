package easy.lenght_of_last_word;

class Solution {
    public int lengthOfLastWord(String s) {
        String[] words = s.trim().split(" ");
        return words[words.length - 1].length();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.lengthOfLastWord("   fly me   to   the moon  "));
    }
}