class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        int sum = 0;
        for(int i : apple){
            sum += i;
        }

        Arrays.sort(capacity);

        int cnt = 0;
        for(int i = capacity.length - 1; i >= 0; i--){
            sum -= capacity[i];
            cnt += 1;
            if(sum <= 0) return cnt;
        }
        return cnt;
    }
}