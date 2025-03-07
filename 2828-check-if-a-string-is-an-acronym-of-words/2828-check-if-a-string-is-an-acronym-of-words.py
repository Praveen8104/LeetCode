class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        l=""
        for i in words:
           for j in range(len(i)):
                l+=i[0]
                break
        if len(words)==len(s) and l==s:
            return True
        else:
            return False