class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int c = nums[i];
            int sum = 0;
            while (c > 0) {
                int rem = c % 10;
                sum = sum + rem;
                c = c / 10;
            }
            if (sum == i)
                return i;
        }
        return -1;
    }
}