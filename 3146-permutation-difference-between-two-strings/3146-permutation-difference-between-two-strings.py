class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return 0

        diff = 0
        for i in s:
            x = s.index(i)
            y = t.index(i)
            diff += abs( x - y)
        
        return diff