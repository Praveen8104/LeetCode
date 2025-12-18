class Solution {
    public int minElement(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int sum = 0;
            while (num > 0) {
                int c = num % 10;
                sum = sum + c;
                num = num / 10;
            }
            nums[i] = sum;
        }
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            min = Math.min(min, nums[i]);
        }
        return min;
    }
}