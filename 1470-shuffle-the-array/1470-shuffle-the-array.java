class Solution {
    public int[] shuffle(int[] nums, int n) {
        int i = 0, j = n;
        int[] res = new int[nums.length];
        int ind = 0;
        while(j<nums.length){
            res[ind++] = nums[i++];
            res[ind++] = nums[j++];
        }
        return res;
    }
}