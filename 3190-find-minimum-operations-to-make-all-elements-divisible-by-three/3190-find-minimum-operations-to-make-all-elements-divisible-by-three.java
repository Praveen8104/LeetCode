class Solution {
    public int minimumOperations(int[] nums) {
        int cnt = 0;
        for(int a : nums){
            if (a%3 != 0 ){
                cnt++;
            }
        }
        return cnt;
    }
}