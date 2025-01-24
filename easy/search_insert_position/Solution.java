package easy.search_insert_position;

class Solution {
    // public int searchInsert(int[] nums, int target) {
    // for (int i = 0; i < nums.length; i++) {
    // if (nums[i] >= target) {
    // return i;
    // }
    // }
    // return nums.length;
    // }

    // Binary search
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (nums[mid] >= target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        int[] nums = { 1, 3, 5, 6 };
        System.out.println(s.searchInsert(nums, 5));
        System.out.println(s.searchInsert(nums, 2));
        System.out.println(s.searchInsert(nums, 7));
    }
}