class Solution {
    public String clearDigits(String s) {
        StringBuilder sb = new StringBuilder(s);
        for (int i = 0; i < sb.length(); i++) {
            int ind = sb.charAt(i) - '0';
            if (ind >= 0 && ind <= 9) { 
                sb = sb.delete(i - 1, i + 1);
                i -= 2;
            }
        }
        return sb.toString(); 
    }
}