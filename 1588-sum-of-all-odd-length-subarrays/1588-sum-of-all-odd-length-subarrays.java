class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int sum = 0;
        int n = arr.length;
        for(int i = 0; i < n; i++){
            int r = (i + 1) * (n - i);
            r = (r + 1) / 2;
            sum += arr[i] * r;
        }
        return sum;
    }
}