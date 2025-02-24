class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = set(allowed)
        c = 0
        for i in words:
            for j in i:
                if j not in allowed:
                    c += 1
                    break
        return len(words) - c
            
        