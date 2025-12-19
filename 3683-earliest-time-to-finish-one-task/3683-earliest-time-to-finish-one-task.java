class Solution {
    public int earliestTime(int[][] tasks) {
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < tasks.length; i++){
            for(int j = 1; j < tasks[i].length; j++){
                int diff = tasks[i][j - 1] + tasks[i][j];
                min = Math.min(diff, min);
            }
        }
        return min;
    }
}