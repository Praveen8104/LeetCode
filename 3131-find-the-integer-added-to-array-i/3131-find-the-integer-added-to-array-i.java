class Solution {
    public int addedInteger(int[] nums1, int[] nums2) {
        int a = 0, b = 0;
        for (int i = 0; i < nums1.length; i++) {
            a += nums1[i];
            b += nums2[i];
        }
        return (b - a) / nums1.length;
    }
}