class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        str1 = ''
        for i in words:
            str1 += i
            if str1 == s:
                return True
            if not s.startswith(str1):
                break
        return False