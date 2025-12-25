class Solution {
    public int lengthOfLongestSubstring(String s) {
        if ( s == null || s.length() == 0 ) return 0;

        int[] visited = new int[256];

        Arrays.fill(visited, -1);

        int left = 0, right = 0, maxlen = 0;

        while( right < s.length() ){
            char ch = s.charAt(right);

            if (visited[ch] >= left){
                left = visited[ch] + 1;
            }

            visited[ch] = right;

            int len = right - left + 1;
            maxlen = Math.max(maxlen, len);
            right++;
        }
        return maxlen;
    }
}