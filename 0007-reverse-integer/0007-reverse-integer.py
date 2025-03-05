class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if s[0]!=0 and s[0]!='-':
            rev=int(s[::-1])
            if rev>pow(-2,31) and rev<pow(2,31):
                return (rev)
            else:
                return 0
        else:
            rev=int('-'+s[:0:-1])
            if rev>pow(-2,31) and rev<pow(2,31):
                return rev
            else:
                return 0
       