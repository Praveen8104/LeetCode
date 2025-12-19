class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        int ans1 = 0, ans2 = 0;
        for(int i : nums1){
            for(int j : nums2){
                if(i == j){
                    ans1++;
                    break;
                }
            }
        }

        for(int i : nums2){
            for(int j : nums1){
                if(i == j){
                    ans2++;
                    break;
                }
            }
        }       

        return new int[]{ans1, ans2}; 
    }
}