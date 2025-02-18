class Solution {
    public int myAtoi(String s) {
        int sign = 1;
        long result = 0;

        int i = 0;

        while (i < s.length() && s.charAt(i) == ' ')
            i++;

        if (i < s.length() && s.charAt(i) == '-') {
            sign = -1;
            i++;
        }else if (i < s.length() && s.charAt(i) == '+')
            i++;

        while (i<s.length()) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                result = result * 10 + (long)(s.charAt(i) - '0');
            } else
                break;
            i++;

            if (result > Integer.MAX_VALUE) {
                if (sign == -1)
                    return Integer.MIN_VALUE;
                return Integer.MAX_VALUE;
            }
        }

        result *= sign;

        return (int)result;
    }
}