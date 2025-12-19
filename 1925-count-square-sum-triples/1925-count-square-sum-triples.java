class Solution {
    public int countTriples(int n) {
        int ans = 0;

        for (int i = 1; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                double tri = Math.sqrt(Math.pow(i, 2) + Math.pow(j, 2));
                if (tri % 1 == 0 && (int) tri <= n) {
                    ans += 2;
                }
            }
        }
        return ans;
    }
}