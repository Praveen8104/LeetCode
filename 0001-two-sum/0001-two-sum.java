class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] p=new int[2];
       for(int i=0;i<nums.length-1;i++)
       {
           for(int j=i+1;j<nums.length;j++)
           {
               if(nums[i]+nums[j]==target)
               {
                    p[0]=i;
                    p[1]=j;
               }
           }
       } 
       return p;
    }
}