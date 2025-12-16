class Solution {
    public int[] numberGame(int[] nums1) {
        int[] nums = nums1.clone();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i+=2){
            int temp = nums[i];
            nums[i] = nums[i + 1];
            nums[i + 1] = temp;
        }
        return nums;
    }
}