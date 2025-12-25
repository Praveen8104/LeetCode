class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        int j = 0;
        long ans = 0;
        for(int i = happiness.length -1 ; i >= 0; i--){
            ans += Math.max(happiness[i] - j, 0);
            j++;
            k--;
            if(k == 0) return ans;
        }
        return ans;
    }
}