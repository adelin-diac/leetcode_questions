package easy.sqrt_x;

public class Solution {
    // public int mySqrt(int x) {
    // if (x <= 0) {
    // return 0;
    // }
    // int closest = 1;
    // for (int i = 2; i <= x / 2; i++) {
    // if (x / i >= i) {
    // closest = i;
    // }
    // }
    // return closest;
    // }

    // Binary Search
    public int mySqrt(int x) {
        if (x <= 0) {
            return 0;
        }
        int l = 1;
        int r = x;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            long square = (long) mid * mid;

            if (square == x) {
                return mid;
            } else if (square < x) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return r;

    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // System.out.println(s.mySqrt(16));
        // System.out.println(s.mySqrt(24));
        // System.out.println(s.mySqrt(26));
        // System.out.println(s.mySqrt(2147395599));
        System.out.println(s.mySqrt(2147395600));
    }
}
