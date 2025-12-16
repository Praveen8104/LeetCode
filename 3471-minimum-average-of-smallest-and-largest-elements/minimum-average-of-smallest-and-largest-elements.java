class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);

        int left = 0, right = nums.length - 1;
        double minavg = Double.MAX_VALUE;
        while(left < right){
            double avg = (nums[left] + nums[right]) / 2.0;
            minavg = Math.min(avg, minavg);
            left++;
            right--;
        }
        return minavg;
    }
}