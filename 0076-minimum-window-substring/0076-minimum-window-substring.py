class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        
        for c in t:
            d[c] += 1
        
        cnt = len(d) 
        
        ans = ""
        d1 = defaultdict(int)
        l = 0
        cnt1 = 0
        for r in range(len(s)):
            d[s[r]] -= 1
            if d[s[r]] == 0: 
                cnt1 += 1
            while cnt1 == cnt: 
                if not ans or len(ans) > r - l + 1:
                    ans = s[l:r+1]
                d[s[l]] += 1
                if d[s[l]] == 1:
                    cnt1 -= 1
                l += 1
    
        return ans