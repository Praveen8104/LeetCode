class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        dick ={}
        c=0
        for i in s:
            fu=str(sorted(i))
            if fu not in dick:
                dick[fu]=[]
            dick[fu].append(i)
        return list(dick.values())