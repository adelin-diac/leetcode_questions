package easy.plus_one;

class Solution {

    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i > 0; i++) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int x[] = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };
        x = s.plusOne(x);
        for (int i = 0; i < x.length; i++) {
            System.out.println(x[i]);
        }

    }
}
