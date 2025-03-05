class Solution {
    public static boolean isPalindrome(int x) {
        int temp=x,rem,rev=0;
        if(x<0)
        return false;
        while(x!=0)
        {
            rem=x%10;
            rev=rev*10+rem;
            x/=10;
        }
        return (temp==rev);
    }
}